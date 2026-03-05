# GA4 — Q18: DuckDB Data Preparation for RetailCo Analytics

## Problem Summary

RetailCo wants to analyze orders coming from their **LATAM region**.  
The database contains a table named `orders` with the following columns:

- **order_id** – Unique order identifier (INTEGER)
- **customer** – Customer name (some rows contain `NULL`)
- **order_date** – Date of the order (DATE)
- **product** – Product name (VARCHAR)
- **amount** – Order value as a decimal (range 0–900)
- **region** – One of `US`, `EU`, `APAC`, `LATAM`

The task is to write **a single DuckDB SQL query** that performs several data preparation steps and aggregation.

---

# Required Transformations

The query must perform the following operations:

### 1. Filter Region
Only orders belonging to the **LATAM region** should be included.

```
WHERE region = 'LATAM'
```

---

### 2. Replace NULL Customers

Some rows contain missing customer names (`NULL`).  
These must be replaced with the string **"Unknown"** using `COALESCE`.

Example:

```
COALESCE(customer, 'Unknown')
```

This ensures the dataset contains **no NULL customer values**.

---

### 3. Create Price Bands

Each order must be categorized into a **price band** using a `CASE` expression.

Rules:

| Condition | Band |
|---|---|
| amount > 720 | high |
| amount > 323 | medium |
| otherwise | low |

Example:

```
CASE
    WHEN amount > 720 THEN 'high'
    WHEN amount > 323 THEN 'medium'
    ELSE 'low'
END
```

---

### 4. Aggregate Medium Band Orders

The final output must return **exactly one row** representing the **medium price band**.

Two values must be computed:

- **order_count** → total number of medium orders
- **total_amount** → total order value for medium orders

The total must be **rounded to two decimal places** using:

```
ROUND(SUM(amount), 2)
```

---

# Query Design

The solution uses a **subquery** to perform data preparation first:

1. Replace NULL values
2. Compute price bands
3. Filter LATAM orders

Then the outer query filters **only the `medium` band** and calculates the final aggregates.

This approach keeps the logic clear and modular.

---

# Final DuckDB SQL Query

```sql
SELECT
    COUNT(*) AS order_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM (
    SELECT
        COALESCE(customer, 'Unknown') AS customer_name,
        amount,
        CASE
            WHEN amount > 720 THEN 'high'
            WHEN amount > 323 THEN 'medium'
            ELSE 'low'
        END AS price_band
    FROM orders
    WHERE region = 'LATAM'
) t
WHERE price_band = 'medium';
```

---

# Explanation

### Subquery (`t`)

The inner query performs **data preparation**:

- `COALESCE(customer, 'Unknown')` replaces NULL customers.
- `CASE` assigns each order a **price_band**.
- `WHERE region = 'LATAM'` filters only LATAM orders.

### Outer Query

The outer query performs **aggregation**:

- `COUNT(*)` counts medium-price orders.
- `SUM(amount)` calculates the total order value.
- `ROUND(..., 2)` ensures the result has **two decimal places**.

---

# Expected Output

The query returns **exactly one row** containing:

| order_count | total_amount |
|---|---|
| number of medium orders | sum of medium order values |

---
