# Dataset sources and provenance

## Scope

The project source-register document supplied by the project owner records:

- **41 core source-register entries**
- **148 additional unique URLs**
- **Five broad source categories**
- District-level, taluka-level, village-level and sector-specific material relevant to Palghar district, Maharashtra

The register includes sources associated with the District Collectorate and district administration, Panchayat Samiti/taluka portals, Central and Maharashtra State Government departments, Census/village-level information, and secondary or academic references.

## How to interpret this register

This file documents provenance at the project level. It is not a run manifest and does not prove that every listed URL was downloaded, parsed, or included in a particular model-training run.

The supplied training notebook's direct workflow is to accept PDF inputs, extract page-wise text with PyMuPDF, prepare a text dataset, split it into training and validation portions, tokenize/chunk it, and train a causal language model. The exact documents uploaded during a run should be recorded separately with filenames, retrieval dates, checksums and source URLs.

## Source-quality and date considerations

- Record the department/publisher, source URL, reference year and access date for each source.
- Distinguish official government publications from secondary directories, aggregators and academic material.
- Preserve conflicting values with a note identifying the competing sources; do not silently choose one.
- Represent unavailable indicators as missing/unknown, not as zero.
- Palghar district was formed on 1 August 2014 from the former Thane district. Some Census 2011 statistics may therefore be reported for the earlier administrative geography or constituent sub-districts. Do not label those figures as a post-2014 Palghar district census without qualification.
- Validate current administrative boundaries, facility lists and scheme details before presenting them as current.

## Recommended run-level manifest

For each actual training run, maintain a machine-readable manifest with at least:

| Field | Description |
|---|---|
| `run_id` | Unique identifier for the training run |
| `source_id` | Stable identifier from the source register |
| `source_url` | Original URL, where applicable |
| `local_filename` | Exact file supplied to the notebook |
| `publisher` | Department or publisher |
| `reference_year` | Period covered by the source |
| `accessed_at` | Date the source was retrieved |
| `sha256` | File checksum |
| `used_in_training` | Whether the file was actually included in that run |
| `notes` | Coverage, conflicts, limitations or extraction issues |

## Data handling recommendation

Keep original PDFs immutable. Store extracted text and derived datasets separately, retain source-page references where possible, and document all transformations. Do not commit restricted, personal, sensitive or copyrighted source material unless redistribution is permitted.

> The complete source register remains the authoritative project inventory. This summary intentionally avoids inventing individual source titles or claiming that every catalogue URL was directly ingested by the notebook.
