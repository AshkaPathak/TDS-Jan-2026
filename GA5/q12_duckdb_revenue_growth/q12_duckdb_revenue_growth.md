# GA5 — Q12: DuckDB — Month with Highest Revenue Growth

## Problem Summary

We are given a DuckDB table named `sales` with approximately 480 rows and 2 columns:

- `sale_date` — stored as a string in mixed date formats:
  - `YYYY-MM-DD`
  - `DD/MM/YYYY`
  - `Month DD, YYYY`
- `amount` — revenue from the sale as a decimal number

The task is to write a DuckDB SQL query to find the **month in 2024 with the highest month-over-month (MoM) revenue growth rate**.

The query must:

1. Parse the mixed date formats correctly
2. Aggregate total revenue per calendar month (`YYYY-MM`)
3. Compute MoM growth using the previous month’s revenue
4. Return exactly **1 row** with:
   - `month`
   - `mom_growth_pct`

---

## Approach

The solution is built in three stages:

### 1. Parse mixed date formats

Since the DuckDB version used in the portal does not support `TRY_STRPTIME`, date parsing is handled using `CASE` with pattern matching:

- `____-__-__` → `%Y-%m-%d`
- `__/__/____` → `%d/%m/%Y`
- otherwise → `%B %d, %Y`

This ensures every `sale_date` is converted into a valid date.

### 2. Aggregate monthly revenue

After parsing, the dates are converted into `YYYY-MM` format using `STRFTIME(parsed_date, '%Y-%m')`.

Revenue is then aggregated month-wise using:

```sql
SUM(amount)
```

Only rows from calendar year 2024 are included.

### 3. Compute MoM growth

The previous month’s revenue is obtained using the window function:

```sql
LAG(revenue) OVER (ORDER BY month)
```

The MoM growth percentage is then computed as:

\[
\text{MoM Growth \%} = \frac{\text{current revenue} - \text{previous revenue}}{\text{previous revenue}} \times 100
\]

The final result is ordered by growth percentage descending and limited to 1 row.

---

## Final SQL Query

```sql
WITH parsed AS (
    SELECT
        CASE
            WHEN sale_date LIKE '____-__-__'
                THEN STRPTIME(sale_date, '%Y-%m-%d')
            WHEN sale_date LIKE '__/__/____'
                THEN STRPTIME(sale_date, '%d/%m/%Y')
            ELSE STRPTIME(sale_date, '%B %d, %Y')
        END AS parsed_date,
        amount
    FROM sales
),
monthly AS (
    SELECT
        STRFTIME(parsed_date, '%Y-%m') AS month,
        SUM(amount) AS revenue
    FROM parsed
    WHERE parsed_date >= DATE '2024-01-01'
      AND parsed_date < DATE '2025-01-01'
    GROUP BY 1
),
mom AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) AS prev_revenue
    FROM monthly
)
SELECT
    month,
    ROUND(((revenue - prev_revenue) / prev_revenue) * 100, 2) AS mom_growth_pct
FROM mom
WHERE prev_revenue IS NOT NULL
ORDER BY mom_growth_pct DESC
LIMIT 1;
```

---

## Why This Works

This query works correctly because:

- It handles all three date formats explicitly
- It converts dates into a consistent monthly format
- It aggregates revenue per month before computing growth
- It uses `LAG()` to access the previous month’s revenue
- It returns exactly the required output columns:
  - `month`
  - `mom_growth_pct`

---

## Key SQL Concepts Used

- `CASE`
- `STRPTIME`
- `STRFTIME`
- `SUM`
- `GROUP BY`
- `LAG() OVER (...)`
- `ROUND`
- `ORDER BY ... DESC`
- `LIMIT 1`

---

## Conclusion

The correct solution required:

- Handling mixed date formats safely
- Aggregating revenue month by month
- Using a window function to compute month-over-month growth
- Returning the highest-growth month as a single-row result

This makes the query fully aligned with the problem’s output requirements.
