# GA4 — Q5: OpenRefine Supplier Spend Consolidation

## Problem Summary

Orbit Commerce exported supplier invoices from their ERP system. However, the dataset contains inconsistent supplier names (punctuation, casing, abbreviations), duplicate invoices (resubmissions), currency formatting issues, and mixed status/category values.

The objective was to clean the dataset using OpenRefine and compute the total Approved spend (USD) for Lumen Analytics in the Logistics category.

---

## Dataset

File used:
q-openrefine-supplier-spend.csv

---

## Cleaning Workflow in OpenRefine

### 1) Import CSV
- Load the dataset into OpenRefine.
- Verify column types.

### 2) Trim Whitespace
For all textual columns:
Edit cells → Common transforms → Trim leading and trailing whitespace

Applied to:
- supplier_name
- category
- status
- invoice_id

---

### 3) Cluster Supplier Names

Column: supplier_name

Use:
- Key collision (fingerprint, ngram-fingerprint)
- Nearest neighbour (Levenshtein)

Merge all variants into canonical name:
Lumen Analytics

Variants merged:
- Lumen-Analytics
- LumenAnalytic
- Lumen Analytix
- LumenAnalytics
- Lumen Analytics

---

### 4) Remove Duplicate Invoices

Facet on:
invoice_id

Keep only one row per invoice_id (remove resubmissions).

---

### 5) Clean amount_usd Column

Use GREL:

value.replace(/[^0-9.]/, "")

Then convert the column to Number type.

---

### 6) Filter Required Rows

Apply filters:
- supplier_name = "Lumen Analytics"
- category = "Logistics"
- status = "Approved"

---

### 7) Compute Total Spend

Use numeric facet or export and sum the cleaned numeric column.

---

## Final Answer

Total Approved spend (USD) for Lumen Analytics in Logistics after cleaning:

23765.47

---

## Conclusion

✔ Supplier variants clustered correctly  
✔ Duplicate invoice_id rows removed  
✔ Currency values cleaned and converted  
✔ Filters applied after cleaning  
✔ Final validated total: 23765.47 USD
