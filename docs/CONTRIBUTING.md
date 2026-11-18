# Contributing

Thanks for helping improve PalgharGPT.

## Before submitting changes

- Keep project claims consistent with the training notebook.
- Do not describe continued causal language-model training as supervised Q&A fine-tuning.
- Do not claim RAG, live retrieval, vector search or source citations unless those capabilities are implemented and tested.
- Preserve source URLs, publishers, reference years and access dates.
- Clearly label secondary sources and conflicting values.
- Never convert missing data into zero or silently overwrite conflicting source values.
- Do not commit private data, credentials, raw PDFs or large trained checkpoints.

## Pull requests

Include:
1. A concise explanation of the change.
2. The files and training/data workflow affected.
3. Validation steps performed.
4. Any change to dependencies, source provenance or model behaviour.
5. Updated documentation when implementation or data assumptions change.

## Style

Prefer clear, reproducible code and documentation. Keep experiments separate from production-facing interfaces, and document unverified assumptions explicitly.
