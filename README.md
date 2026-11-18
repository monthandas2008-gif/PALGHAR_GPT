# PalgharGPT

**A district-domain language-model adaptation project for Palghar, Maharashtra.**

PalgharGPT explores adapting `Qwen/Qwen2.5-1.5B-Instruct` to Palghar district material using 4-bit quantization and LoRA adapters (QLoRA-style parameter-efficient training).

> **Training-method clarification:** The project notebook workflow is continued causal language-model training on extracted document text. It is not a retrieval-augmented generation (RAG) system, does not use a vector database, and should not be described as supervised question-answer fine-tuning unless a separate Q&A dataset and training pipeline are added.

## Repository structure

```text
PALGHAR_GPT/
├── README.md
├── app.py
├── requirements.txt
├── .gitignore
├── docs/
│   ├── CONTRIBUTING.md
│   ├── DATASET_SOURCES.md
│   ├── MODEL_CARD.md
│   └── REPRODUCIBILITY.md
├── notebooks/
│   └── README.md
└── .github/
    └── workflows/
        └── validate.yml
```

**Training notebook status:** The original notebook is not yet present in this GitHub repository. See [notebooks/README.md](notebooks/README.md) for the exact filename and guidance. Do not treat a placeholder as the original training artifact. When available, the original notebook is the source of truth for exact training parameters and outputs.

## Model and workflow

- **Base model:** `Qwen/Qwen2.5-1.5B-Instruct`
- **Adaptation:** LoRA adapters with 4-bit NF4 quantization (QLoRA-style)
- **Training objective:** causal language modelling on extracted district-document text
- **Document extraction:** PyMuPDF
- **Data handling:** page-wise text extraction, train/validation split, tokenization and sequence chunking
- **Training ecosystem:** PyTorch, Hugging Face Transformers, PEFT, bitsandbytes and Datasets
- **Typical execution environment:** Google Colab with a compatible CUDA GPU

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/monthandas2008-gif/PALGHAR_GPT.git
cd PALGHAR_GPT
```

### 2. Create an environment

Python 3.10 or 3.11 is recommended. Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

For GPU training/inference, install a PyTorch build compatible with the CUDA runtime. bitsandbytes support depends on operating system, CUDA version and hardware.

### 3. Run the inference interface

After training and saving a PEFT adapter, set its directory and launch Streamlit:

```bash
# Linux/macOS
export PALGHARGPT_ADAPTER_DIR="path/to/your/adapter"

# Windows PowerShell
$env:PALGHARGPT_ADAPTER_DIR="path/to/your/adapter"

streamlit run app.py
```

The app expects a compatible CUDA GPU and a PEFT adapter directory. The default base model can be overridden with `PALGHARGPT_BASE_MODEL`. The app is a basic inference interface; it does not add retrieval or source citations.

### 4. Run the training notebook

The original notebook is not currently committed. Add the original project notebook at `notebooks/PalgharGPT_QLoRA_Training.ipynb` before following the training workflow. See [notebooks/README.md](notebooks/README.md). The original notebook requests three PDF inputs; do not assume the source catalogue URLs were automatically downloaded.

The PDFs, derived datasets and trained model weights are intentionally not committed. Keep source documents and generated checkpoints in local/Colab storage or an approved model-artifact store.

## Dataset provenance

The supplied project source-register document is described as containing **41 core source entries** and **148 additional unique URLs** across five categories. See [Dataset sources and provenance](docs/DATASET_SOURCES.md).

The source register is a provenance catalogue, not a run manifest. A URL appearing in the register does not prove that the notebook fetched that URL or used its contents in a particular training run. Record the exact files used in each run, including source URL (if any), retrieval date and SHA-256 checksum.

## Outputs

The training workflow is expected to create extracted text/dataset files, tokenized training data, training/evaluation outputs and LoRA adapter artifacts. Exact output paths and names must be confirmed from the original notebook cells for the run being reproduced.

## Important limitations

- This is an experimental domain adaptation project, not an official government information service.
- Model outputs can be incomplete, outdated or incorrect; verify important facts against original sources.
- Source documents may have different reference years, coverage and definitions.
- Census 2011 figures may predate Palghar district's formation and require careful geographic interpretation.
- Do not treat missing data as zero or infer that a source-register URL was part of a specific training run without run-level evidence.
- No RAG, live retrieval, source-grounded citation layer or automatic freshness mechanism is implemented by the documented training workflow.

## Responsible use

Do not use generated responses as the sole basis for decisions involving public services, health, finance, legal rights or emergency response. Consult the responsible department and original source.

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md). Document changes to training data, source provenance, model configuration and evaluation.

## License

No license has been specified for this repository. Until a license is added, reuse and redistribution are not automatically granted. Check the licenses and terms of the upstream datasets and base model separately.
