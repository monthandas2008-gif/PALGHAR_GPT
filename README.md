# PalgharGPT

**A district-domain language-model adaptation project for Palghar, Maharashtra.**

PalgharGPT explores adapting `Qwen/Qwen2.5-1.5B-Instruct` to Palghar district material using 4-bit quantization and LoRA adapters (QLoRA-style parameter-efficient training).

> **Training-method clarification:** The supplied notebook implements continued causal language-model training on extracted document text. It is not a retrieval-augmented generation (RAG) system, does not use a vector database, and should not be described as supervised question-answer fine-tuning unless a separate Q&A dataset and training pipeline are added.

## Repository structure

```text
PALGHAR_GPT/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── DATASET_SOURCES.md
│   ├── MODEL_CARD.md
│   ├── REPRODUCIBILITY.md
│   └── CONTRIBUTING.md
└── notebooks/
    └── PalgharGPT_QLoRA_Training.ipynb
```

The training notebook is the source of truth for the implemented training workflow. The documentation describes the workflow and provenance; it does not imply that every upstream URL was automatically downloaded by the notebook.

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

Python 3.10 or 3.11 is recommended. Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

For GPU training, install a PyTorch build compatible with the CUDA runtime on the target machine. bitsandbytes support depends on the operating system, CUDA version and hardware.

### 3. Run the training notebook

Open `notebooks/PalgharGPT_QLoRA_Training.ipynb` in Google Colab or Jupyter. Provide the three PDF inputs requested by the notebook when prompted. Run the cells in order, review the generated text dataset and split, then execute training and evaluation.

The PDFs and trained model weights are intentionally not committed. Keep source documents and generated checkpoints in local/Colab storage or an approved model-artifact store.

## Dataset provenance

The project uses Palghar district development material. The source register supplied for this project records **41 core source entries** and **148 additional unique URLs** grouped across five categories. See [Dataset sources and provenance](docs/DATASET_SOURCES.md).

The source register is a provenance catalogue. A URL appearing in that register does not, by itself, prove that the notebook fetched that URL or used its contents in a training run. The notebook's explicit PDF upload and extraction cells define the direct inputs to the documented run.

## Outputs

The notebook creates intermediate extracted text/dataset files, tokenized training data, training/evaluation outputs and LoRA adapter artifacts. Exact output paths and names should be taken from the notebook cells for the run being reproduced.

## Important limitations

- This is an experimental domain adaptation project, not an official government information service.
- Model outputs can be incomplete, outdated, or incorrect; verify important facts against original sources.
- Source documents may contain different reference years, coverage and definitions.
- Census 2011 figures may predate Palghar district's formation and can require careful interpretation.
- Do not treat missing values as zero or infer that a source-register URL was part of a specific training run without run-level evidence.
- No RAG, live retrieval, source-grounded citation layer or automatic freshness mechanism is implemented by the described notebook.

## Responsible use

Do not use generated responses as the sole basis for decisions involving public services, health, finance, legal rights or emergency response. Consult the responsible department and the original source.

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md). Please document any changes to the training data, source register, model configuration or evaluation process.

## License

No license has been specified for this repository. Until a license is added, reuse and redistribution are not automatically granted. Check the licenses and terms of the upstream datasets and base model separately.
