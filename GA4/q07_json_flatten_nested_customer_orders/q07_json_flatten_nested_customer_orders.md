# GA4 — Q7: JSON Flatten Nested Customer Orders

## Problem Summary

Slingshot Cloud exports customer records as JSONL where:

- Each line represents one customer
- Each customer contains a nested `orders` array
- Each order contains an `items` array

To answer a product analytics request, the dataset must be flattened so that each order item becomes one row.

---

## Objective

Compute the total quantity of **Commerce** items sold:

- Channel: **Marketplace**
- Region: **Europe**
- Date range:  
  2024-02-25 through 2024-03-16 (inclusive)

---

## Dataset

File used:

q-json-customer-flatten.jsonl

---

## Processing Steps

### 1) Stream JSONL file

Process each line individually to avoid loading entire file into memory.

### 2) Explode Nested Arrays

For each customer:
- Iterate through `orders`
- For each order, iterate through `items`
- Emit one logical row per item

Logical flattened structure:

- region
- channel
- order_date
- category
- quantity

---

### 3) Apply Filters

Keep rows where:

- region == "Europe"
- channel == "Marketplace"
- category == "Commerce"
- order_date between 2024-02-25 and 2024-03-16

---

### 4) Aggregate

Sum the `quantity` field.

---

## Final Answer

Total quantity matching criteria:

**6**

---

## Conclusion

✔ Nested arrays flattened correctly  
✔ Filters applied at item level  
✔ Date window respected  
✔ Aggregation verified  
✔ Final validated result: **6**
