# GA4 Q16: Cross-Lingual Entity Disambiguation Dataset

This folder contains the dataset files used by the GA4 Q16 cross-lingual entity disambiguation challenge. The task is to map each document mention to the correct canonical historical entity.

## Dataset

| File | Purpose |
| --- | --- |
| `documents.jsonl` | Document mentions to classify |
| `entity_reference.csv` | Canonical entity metadata |

## Document Format

Each line in `documents.jsonl` is one JSON object with:

- `doc_id`: document identifier such as `DOC-0001`
- `language`: ISO language code
- `year`: event year
- `text`: document excerpt
- `mentioned_name`: name as written in the document
- `source_region`: geographic context

## Entity Reference Format

`entity_reference.csv` contains:

- `entity_id`: canonical ID such as `E001`
- `canonical_name`: standardized English name
- `role`: historical role
- `era`: time period
- `region`: geographic origin

## Intended Method

The full question writeup is in `../q16_cross_lingual_entity_disambiguation.md`. The intended disambiguation method combines:

1. Name normalization and alias matching across languages.
2. Ordinal and title extraction from document text.
3. Region matching between document context and entity metadata.
4. Temporal filtering using `year` and `era`.
5. Special-case handling for repeated royal names and translated names.
6. A scoring system that ranks candidate entities by combined evidence.

The minimal `../solve_q16.py` script currently performs a simpler baseline:

1. Load `entity_reference.csv`.
2. Normalize canonical names and document mentions.
3. Match by direct substring overlap.
4. Fall back to the first entity if no match is found.
5. Write `output.csv` with `doc_id,entity_id`.

## Output Format

The required output is:

```csv
doc_id,entity_id
DOC-0001,E003
DOC-0002,E017
```

## Run

From `GA4/q16_cross_lingual_entity_disambiguation/`:

```bash
python solve_q16.py
```

This generates `output.csv`.
