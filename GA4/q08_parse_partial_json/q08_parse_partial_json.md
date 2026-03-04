# GA4 — Q8: Recovering Sales Data from Partial JSON

## Problem Summary

ReceiptRevive Analytics processes legacy receipt data that has been digitized using OCR.  
Due to damaged receipts, some JSON entries are truncated and the `id` field is missing.

Despite incomplete records, the objective is to accurately extract and aggregate the `sales` values across all 100 rows.

---

## Dataset

File used:

q-parse-partial-json.jsonl

Each row represents one sales entry with expected keys:

- city
- product
- sales
- id (sometimes missing due to truncation)

The task focuses **only on recovering and summing the sales values**.

---

## Data Recovery Approach

### 1) Stream JSON Lines

Process file line-by-line to avoid loading everything into memory.

### 2) Parse Safely

- Handle partially truncated JSON rows
- Extract only the `sales` field
- Ignore missing `id` values

### 3) Data Validation

- Ensure `sales` is numeric
- Skip malformed rows if necessary
- Do not rely on `id` field

### 4) Aggregate

Compute:

total_sales = sum(sales across all valid rows)

---

## Final Answer

Total sales value:

**57430**

---

## Conclusion

✔ JSON streamed safely  
✔ Truncated fields handled gracefully  
✔ Missing IDs ignored  
✔ Sales values recovered accurately  
✔ Final validated total: **57430**
