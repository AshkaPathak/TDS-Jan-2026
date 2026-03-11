# GA5 — Q16: DuckDB — Sales Over Time

## Problem Summary

We are given a DuckDB table named `sales` containing **10,000 rows** with the following columns:

- `timestamp` — time when the sale occurred (stored as text)
- `category` — product category (e.g. Clothing, Home Goods, Electronics)
- `amount` — sale value

The goal is to compute **total sales per category for each hour of the day**, producing a pivoted table where:

- rows represent **hour of day (0–23)**
- columns represent **product categories**
- values represent **total sales amounts rounded to the nearest integer**

Missing hour/category combinations should appear as **0**.

---

# Approach

The solution proceeds in three steps:

### 1. Convert timestamp to a real timestamp

The `timestamp` column is stored as text, so it must be cast to a `TIMESTAMP` type before extracting the hour.

```sql
EXTRACT(HOUR FROM CAST("timestamp" AS TIMESTAMP))
```

---

### 2. Aggregate sales by hour and category

Sales are grouped by:

- hour of the day
- product category

```sql
SUM(amount)
```

This produces total sales per category per hour.

---

### 3. Pivot categories into columns

Since the portal environment did not support the `PIVOT` syntax reliably, the pivot was implemented using **conditional aggregation**:

```sql
SUM(CASE WHEN category = 'Clothing' THEN total_amount END)
```

Each category becomes a separate column.

Missing values are filled using:

```sql
COALESCE(..., 0)
```

---

# Final SQL Query

```sql
WITH hourly AS (
    SELECT
        EXTRACT(HOUR FROM CAST("timestamp" AS TIMESTAMP)) AS hour,
        category,
        SUM(amount) AS total_amount
    FROM sales
    GROUP BY 1, 2
)
SELECT
    h.hour,
    COALESCE(ROUND(SUM(CASE WHEN category = 'Clothing' THEN total_amount END), 0), 0) AS "Clothing",
    COALESCE(ROUND(SUM(CASE WHEN category = 'Home Goods' THEN total_amount END), 0), 0) AS "Home Goods",
    COALESCE(ROUND(SUM(CASE WHEN category = 'Electronics' THEN total_amount END), 0), 0) AS "Electronics"
FROM (
    SELECT generate_series AS hour
    FROM generate_series(0, 23)
) h
LEFT JOIN hourly USING (hour)
GROUP BY h.hour
ORDER BY h.hour;
```

---

# Why This Works

This query correctly produces the required output because it:

- ensures **24 rows (0–23 hours)** using `generate_series`
- aggregates sales totals per category per hour
- pivots category values into columns using conditional aggregation
- fills missing combinations with `0`
- rounds values to the nearest integer
- orders results chronologically by hour

---

# Result

The query returns a **24-row table** with columns:

- `hour`
- `Clothing`
- `Home Goods`
- `Electronics`

Each row represents total hourly sales per category.

---

# Key SQL Concepts Used

- `CAST`
- `EXTRACT`
- `SUM`
- `CASE WHEN`
- `COALESCE`
- `generate_series`
- `GROUP BY`
- `ORDER BY`

---

# Conclusion

By extracting hours from timestamps, aggregating sales by category, and pivoting categories into columns, we generated a complete hourly sales report for each product category.

This approach works reliably even when built-in `PIVOT` syntax is unavailable.
