# GA7 — Q12: Flaw Priority Ranking

## Problem Summary

The task is to read the workbook, exclude all decoy rows where `Is Real = 0`, classify only real flaws into severity levels S1, S2, and S3 using the given compound rule, sort them in the required order, and submit the final tuple list using the numeric part of the Issue ID.

---

## Severity Rules

Apply the rules only to rows where `Is Real = 1`.

### S1 (Critical)
A row is S1 if:

- `Impact >= 80`
- **OR**
- `Impact >= 70 AND Frequency >= 70`

### S2 (Moderate)
A row is S2 if:

- `50 <= Impact <= 79`
- and the S1 compound condition is **not** met

### S3 (Minor)
A row is S3 if:

- `Impact < 50`

---

## Sorting Rules

After classifying only the real flaws:

1. Sort by severity order: **S1 first, then S2, then S3**
2. Within the same severity, sort by **Impact Score descending**
3. If Impact Score ties, sort by **Frequency Score descending**

---

## Filtering Rule

Rows where `Is Real = 0` are decoys and must be completely excluded, even if they have high Impact Score or Frequency Score.

Only real flaws should appear in the final output.

---

## Final Answer

```text
[(4, "S1"), (12, "S1"), (6, "S1"), (13, "S2"), (5, "S2"), (14, "S2"), (15, "S3"), (7, "S3"), (8, "S3")]
