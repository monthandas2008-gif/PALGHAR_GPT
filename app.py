"""Minimal Streamlit interface for a locally saved PalgharGPT LoRA adapter.

Set PALGHARGPT_ADAPTER_DIR to the directory containing the PEFT adapter files.
The base model defaults to Qwen/Qwen2.5-1.5B-Instruct.
"""
import os
import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

BASE_MODEL = os.getenv("PALGHARGPT_BASE_MODEL", "Qwen/Qwen2.5-1.5B-Instruct")
ADAPTER_DIR = os.getenv("PALGHARGPT_ADAPTER_DIR", "outputs/adapter")

st.set_page_config(page_title="PalgharGPT", page_icon="📍", layout="centered")
st.title("PalgharGPT")
st.caption("Experimental language-model adaptation for Palghar district information.")
st.warning(
    "Model-generated answers may be inaccurate or outdated. Verify important "
    "information with the original government or publisher source."
)

@st.cache_resource(show_spinner="Loading model and adapter...")
def load_model():
    if not os.path.isdir(ADAPTER_DIR):
        raise FileNotFoundError(
            f"Adapter directory not found: {ADAPTER_DIR}. "
            "Train the model and set PALGHARGPT_ADAPTER_DIR to the saved adapter path."
        )
    if not torch.cuda.is_available():
        raise RuntimeError(
            "A CUDA-capable GPU is required by this 4-bit inference configuration. "
            "Run in a compatible GPU environment."
        )
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    base = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=quant_config,
        device_map="auto",
        trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(base, ADAPTER_DIR)
    model.eval()
    return tokenizer, model

with st.sidebar:
    st.subheader("Configuration")
    st.write("Base model:", BASE_MODEL)
    st.write("Adapter directory:", ADAPTER_DIR)
    max_tokens = st.slider("Maximum new tokens", 64, 512, 256, 32)
    temperature = st.slider("Temperature", 0.1, 1.2, 0.7, 0.1)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask about Palghar district...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            tokenizer, model = load_model()
            messages = [
                {"role": "system", "content": (
                    "You are PalgharGPT, an experimental assistant about Palghar "
                    "district. Be clear when information is uncertain. Do not invent "
                    "statistics, dates, schemes, or source citations."
                )},
                {"role": "user", "content": prompt},
            ]
            if hasattr(tokenizer, "apply_chat_template"):
                input_text = tokenizer.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True
                )
            else:
                input_text = f"User: {prompt}\nAssistant:"
            inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
            with torch.inference_mode():
                output = model.generate(
                    **inputs,
                    max_new_tokens=max_tokens,
                    do_sample=temperature > 0,
                    temperature=temperature if temperature > 0 else 1.0,
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=tokenizer.eos_token_id,
                )
            answer = tokenizer.decode(
                output[0][inputs["input_ids"].shape[1]:],
                skip_special_tokens=True,
            ).strip()
            st.markdown(answer or "The model returned an empty response.")
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )
        except Exception as exc:
            st.error(f"Unable to generate a response: {exc}")
