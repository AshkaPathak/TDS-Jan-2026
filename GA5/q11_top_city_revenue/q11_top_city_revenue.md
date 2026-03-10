# GA5 — Q11: Top City by Delivered Revenue

## Problem Summary

RetailHub tracks its e-commerce orders in a **SQLite database**.  
The operations team wants to determine **which city generated the highest total revenue from delivered orders in Q3 2024**.

The database is created from the SQL build script:

```
q-datasette-sales-summary.sql
```

The script generates an SQLite database containing an **orders table** with fields such as:

- `order_id`
- `city`
- `quantity`
- `unit_price`
- `status`

Only orders with status **`delivered`** should be considered when calculating revenue.

Revenue for each order is calculated as:

```
revenue = quantity × unit_price
```

The task is to **aggregate the revenue by city and identify the city with the highest total revenue**.

---

# Approach

The solution follows these steps:

1. Build the SQLite database from the SQL script.
2. Query the `orders` table.
3. Filter rows where `status = 'delivered'`.
4. Compute revenue using `quantity * unit_price`.
5. Aggregate revenue by city using `SUM()`.
6. Sort the results in descending order of revenue.
7. Select the top city.

---

# SQL Query Used

```sql
SELECT
    city,
    SUM(quantity * unit_price) AS revenue
FROM orders
WHERE status = 'delivered'
GROUP BY city
ORDER BY revenue DESC
LIMIT 1;
```

---

# Explanation

- **`quantity * unit_price`** computes revenue for each order.
- **`SUM()`** aggregates the revenue for all delivered orders within each city.
- **`GROUP BY city`** ensures revenue is calculated separately for each city.
- **`ORDER BY revenue DESC`** ranks cities from highest to lowest revenue.
- **`LIMIT 1`** returns only the top-performing city.

---

# Result

The query returned:

```
Mumbai | 522848.23
```

Therefore, the city with the **highest total delivered revenue** is:

```
Mumbai
```

---

# Conclusion

By filtering delivered orders and aggregating revenue using SQL, we determined the top-performing city for RetailHub's Q3 deliveries.

Final Answer:

```
Mumbai
```
