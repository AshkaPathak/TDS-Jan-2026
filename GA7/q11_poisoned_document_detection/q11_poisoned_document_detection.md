# GA7 — Q11: Poisoned Document Detection

## Problem Summary

The task is to classify all 9 documents as included or excluded using the selection rule based on Relevance Score and Error Flag, then sort the full list in the required order and submit it as a tuple list using numeric Doc IDs.

---

## Step 1 — Selection Rule

A document is **included ("I")** only if:

- Relevance Score >= 50
- Error Flag = 0

A document is **excluded ("E")** if:

- Relevance Score < 50
- or Error Flag = 1

This means a poisoned document must be excluded even if its relevance score is high.

---

## Step 2 — Apply the Rule to Each Document

After trimming whitespace and parsing the numeric fields:

- DOC-007 → Relevance 94, Error Flag 0 → **I**
- DOC-002 → Relevance 91, Error Flag 0 → **I**
- DOC-008 → Relevance 73, Error Flag 0 → **I**
- DOC-006 → Relevance 57, Error Flag 0 → **I**
- DOC-009 → Relevance 51, Error Flag 0 → **I**
- DOC-003 → Relevance 95, Error Flag 1 → **E**
- DOC-001 → Relevance 45, Error Flag 0 → **E**
- DOC-005 → Relevance 39, Error Flag 0 → **E**
- DOC-004 → Relevance 30, Error Flag 0 → **E**

---

## Step 3 — Sorting Rule

Sort all 9 entries as follows:

1. All **"I"** entries first
2. Then all **"E"** entries
3. Within each group, sort by **Relevance Score descending**

Using that rule:

- Included group: 7, 2, 8, 6, 9
- Excluded group: 3, 1, 5, 4

---

## Final Answer

```text
[(7, "I"), (2, "I"), (8, "I"), (6, "I"), (9, "I"), (3, "E"), (1, "E"), (5, "E"), (4, "E")]
