# Model Card — PalgharGPT

## Overview

PalgharGPT is an experimental domain-adaptation project based on `Qwen/Qwen2.5-1.5B-Instruct`. It uses parameter-efficient LoRA adaptation with 4-bit quantization to explore language-model adaptation to Palghar district development material.

## Model details

| Attribute | Description |
|---|---|
| Base model | `Qwen/Qwen2.5-1.5B-Instruct` |
| Method | LoRA with 4-bit quantization (QLoRA-style) |
| Objective | Continued causal language-model training on document text |
| Domain | Palghar district, Maharashtra |
| Training workflow | PDF text extraction, dataset preparation, tokenization/chunking, training and evaluation |
| Retrieval | No RAG or vector database in the documented notebook |

## Intended use

- Experimental exploration of district-specific language-model adaptation.
- Educational and research demonstrations.
- Drafting or summarising questions for subsequent verification against original sources.

## Out-of-scope use

- Official government advice or authoritative public-service decisions.
- Emergency, medical, legal or financial decision-making.
- Claims requiring live or continuously updated information.
- Source-cited question answering: the described training pipeline does not provide a retrieval/citation layer.

## Data and limitations

The project source register records 41 core entries and 148 additional unique URLs. A source register is not equivalent to a verified training-run manifest. Actual training inputs must be established from the files supplied to a particular notebook run.

Source coverage, publication dates, administrative boundaries and definitions can vary. Census 2011 information may use pre-2014 Thane district geography. The model can memorise outdated or conflicting statements and can generate unsupported details.

## Evaluation

Use held-out document pages and a documented set of representative prompts. Evaluate factual consistency against original source pages, coverage, hallucination rate, refusal behaviour for unsupported questions, and stability across repeated runs. Do not report performance metrics unless they were measured and recorded.

## Ethical and safety considerations

Do not expose personal or sensitive information from source files. Verify rights to use and redistribute all training documents. Clearly label generated responses as model output and provide human review for consequential uses.

## Base model

The base model is maintained by its respective publisher. Follow its model card and license terms in addition to this project's terms.
