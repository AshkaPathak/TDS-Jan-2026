# GA4 — Q16: Cross-Lingual Entity Disambiguation

## Problem

We are given a multilingual historical dataset where each document references a historical ruler in different languages and scripts.  

Each document contains:

- `doc_id`
- `mentioned_name`
- `text`
- `source_region`
- `year`

The task is to correctly map each document to the correct entity in `entity_reference.csv`.

The required output format is:

```
doc_id,entity_id
DOC-0001,E004
DOC-0002,E009
...
DOC-1000,E017
```

The evaluation requires **≥95% accuracy** across 1000 documents.

---

# Approach

The challenge arises from the following issues:

- Cross-lingual names (English, Chinese, Arabic, Russian, etc.)
- Different ordinal formats (Roman numerals, Arabic numerals, Chinese characters)
- Transliteration variations
- Missing ordinal numbers
- Titles such as **“the Great”** or **“the Conqueror”**

To address these issues, the solution combines several heuristics.

---

# 1. Entity Metadata Parsing

The reference dataset is loaded and enriched with additional metadata.

For each entity we extract:

- birth year
- death year
- region
- canonical ordinal number (if present)

Example:

```
Henry VIII → ordinal = 8
Peter III → ordinal = 3
```

Roman numerals and CJK numerals are converted to integers.

---

# 2. Ordinal Extraction from Documents

Documents may express ordinals in several formats:

Examples:

| Format | Example |
|------|------|
Roman numerals | `Henry VIII`
Arabic numerals | `Louis 14`
Chinese | `十六世`
Arabic | `الثالث`

The solver detects and converts these to integers.

---

# 3. Region Matching

Each document contains `source_region`.

Entities are strongly filtered using region matching:

```
France → French monarchs
Russia → Russian tsars
England / Britain → British monarchs
```

A heavy scoring penalty is applied if regions do not match.

---

# 4. Temporal Filtering

Each entity has a life span:

```
birth_year ≤ document_year ≤ death_year
```

A tolerance window of ±10 years is allowed.

This prevents incorrect matches between rulers of different centuries.

---

# 5. Alias Detection

Historical figures appear in many languages.

Example:

```
Peter → Пётр → Pedro → 彼得
William → Guillaume → Wilhelm → 威廉
Alexander → Александр → 亚历山大
```

A multilingual alias dictionary is used to detect these variants.

Each match increases the entity score.

---

# 6. Special Title Handling

Some rulers are identified primarily through titles.

### The Great

Examples:

- Frederick the Great
- Peter the Great
- Catherine the Great

Many languages translate this phrase differently.

Examples:

```
Great
Grande
Velikiy
Wielki
大帝
伟大
```

Documents containing these markers boost the corresponding entities.

---

### The Conqueror

Example:

```
William the Conqueror
```

In some documents the ordinal is missing and only the title appears.

Markers like:

```
conqueror
conquistador
zavoevatel
征服者
```

directly map to **William I of England**.

---

# 7. Scoring System

Each entity receives a score based on multiple signals:

| Signal | Score Effect |
|------|------|
Region match | +300 |
Region mismatch | −500 |
Year within lifespan | +140 |
Ordinal match | +200 |
Ordinal mismatch | −120 |
Alias detection | +40 |
"The Great" marker | +180 |
"Conqueror" marker | +400 |

The entity with the **highest score** is selected.

---

# Algorithm Workflow

```
for each document:

    extract ordinal from name/text
    compute entity score for all candidates

    score based on:
        region match
        lifespan overlap
        ordinal match
        alias matches
        title markers

    choose entity with highest score
```

---

# Output Generation

Predictions are written to:

```
output.csv
```

Format:

```
doc_id,entity_id
DOC-0001,E004
DOC-0002,E009
...
DOC-1000,E017
```

The rows are sorted by `doc_id`.

---

# Final Result

The improved rule-based disambiguation system achieved:

```
Accuracy: ≥95%
```

which satisfies the evaluation requirement.

---

# Implementation

Main script:

```
solve_q16.py
```

The script:

1. Loads the entity reference dataset
2. Parses ordinal numbers
3. Detects multilingual aliases
4. Applies rule-based scoring
5. Generates the final prediction CSV

---

# Running the Solver

```
python solve_q16.py
```

Verify output:

```
wc -l output.csv
```

Expected result:

```
1001 output.csv
```

(1000 predictions + header)

---

# Repository Structure

```
GA4/
└── q16_cross_lingual_entity_disambiguation
    ├── solve_q16.py
    ├── output.csv
    ├── q16_cross_lingual_entity_disambiguation.md
    └── q-cross-lingual-entity-disambiguation-server
        ├── documents.jsonl
        ├── entity_reference.csv
        └── README.md
```

---

# Conclusion

The solution successfully performs cross-lingual historical entity disambiguation using:

- multilingual alias matching
- ordinal extraction
- region filtering
- lifespan constraints
- title-based heuristics

This hybrid rule-based approach achieves the required **≥95% accuracy** on the evaluation dataset.
