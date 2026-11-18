# Training notebook

The training notebook used in the project is a Google Colab/Jupyter notebook. It is not currently included in this GitHub commit because the repository publishing connection accepts UTF-8 text files, while the original notebook needs to be transferred as a complete notebook artifact.

Use the original project notebook supplied by the project owner. Do not substitute a newly generated or simplified notebook: the original cells are the source of truth for the exact training configuration and workflow.

When adding it to this directory, retain its original code and outputs as appropriate, remove only secrets or personally identifying runtime data, and name it:

`PalgharGPT_QLoRA_Training.ipynb`

The notebook workflow described in the repository documentation includes PDF text extraction, dataset preparation, train/validation splitting, tokenization/chunking, QLoRA-style adapter training, evaluation and saving adapter artifacts.
