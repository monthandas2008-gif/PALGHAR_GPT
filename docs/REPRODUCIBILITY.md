# Reproducibility notes

## Environment

The notebook is designed for a Python environment with a compatible CUDA GPU. Google Colab is the intended convenient execution environment. Exact compatibility depends on the installed versions of PyTorch, CUDA, Transformers, PEFT and bitsandbytes.

Install project dependencies using:

```bash
pip install -r requirements.txt
```

For GPU training, select the PyTorch build that matches the runtime's CUDA environment.

## Reproduction procedure

1. Clone this repository and open `notebooks/PalgharGPT_QLoRA_Training.ipynb`.
2. Record the execution date, runtime type, GPU model, Python version and package versions.
3. Supply the same three PDF inputs used by the target experiment.
4. Record each input filename, source URL, retrieval date and SHA-256 checksum.
5. Execute notebook cells in order, preserving the generated extraction and dataset artifacts.
6. Record the train/validation split, tokenizer settings, sequence length, quantization settings, LoRA configuration, training arguments and random seed as configured in the notebook.
7. Save the adapter, tokenizer/configuration metadata and evaluation outputs.
8. Run the same evaluation prompts against the saved adapter and preserve the outputs.

## Reproducibility caveats

- GPU kernels and library versions can introduce small run-to-run differences.
- A random seed alone does not guarantee bitwise-identical training.
- Re-downloading source PDFs later may yield changed documents; checksums are needed to identify exact inputs.
- Do not infer a training configuration from a README if the notebook cell differs. The notebook is authoritative for the actual run.
- Record any manual edits to extracted text or dataset files.

## Suggested experiment record

Maintain a JSON or YAML record containing the run ID, source manifest, package versions, hardware, random seed, model identifier, quantization and LoRA settings, training arguments, output artifact identifiers and evaluation results.
