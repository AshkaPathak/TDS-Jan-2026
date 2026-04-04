# GA7 — Q13: Chart Error Detection & Severity Ranking

## Problem Summary

The task is to process chart issue data, filter only genuine errors where `Is Error = 1`, classify them into severity levels based on `Error Score`, and output a correctly sorted tuple list using numeric Issue IDs.

---

## Step 1 — Data Cleaning

- Trim whitespace from all columns
- Parse `Error Score`, `Visibility Score`, and `Is Error` as integers
- Ignore metadata columns
- Use only the numeric part of the Issue ID

---

## Step 2 — Filtering Rule

Keep only rows where:

- `Is Error = 1`

Exclude all rows where:

- `Is Error = 0`

False-positive rows must not appear in the final tuple list.

---

## Step 3 — Severity Classification

Apply severity only to genuine errors:

- **S1 (Critical):** `Error Score >= 80`
- **S2 (Moderate):** `50 <= Error Score <= 79`
- **S3 (Minor):** `Error Score < 50`

---

## Step 4 — Sorting Rules

Sort the genuine errors as follows:

1. `S1` first, then `S2`, then `S3`
2. Within the same severity, sort by `Error Score` descending
3. If `Error Score` ties, sort by `Visibility Score` descending

This tie rule matters for the two rows with `Error Score = 93`, where the row with higher `Visibility Score` must come first.

---

## Final Answer

```text
[(11, "S1"), (2, "S1"), (10, "S1"), (1, "S2"), (15, "S2"), (7, "S2"), (8, "S3"), (13, "S3"), (4, "S3")]
