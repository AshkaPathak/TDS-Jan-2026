# GA6 — Q13: Latency SLA Checker

## Problem Summary
We are given an `api_logs` table containing:
- `endpoint`
- `latency_ms`
- `is_error`
- `logged_at`

We must compute **one row per endpoint** with:
- p50 (median latency)
- p95 latency
- p99 latency
- error rate (%)
- SLA status (PASS/FAIL)
- violated SLAs (comma-separated list)

---

## SLA Conditions

| Metric        | Condition     |
|--------------|--------------|
| p50 latency  | ≤ 50 ms      |
| p95 latency  | ≤ 400 ms     |
| p99 latency  | ≤ 1000 ms    |
| error rate   | ≤ 1.0 %      |

---

## Step-by-Step Approach

### Step 1 — Compute Percentiles
DuckDB provides:
- `PERCENTILE_CONT(0.5)` → p50
- `PERCENTILE_CONT(0.95)` → p95
- `PERCENTILE_CONT(0.99)` → p99

All computed using:
`PERCENTILE_CONT(x) WITHIN GROUP (ORDER BY latency_ms)`

---

### Step 2 — Compute Error Rate
We use:
`COUNT(*) FILTER (WHERE is_error = true) * 100.0 / COUNT(*)`

This gives percentage directly.

---

### Step 3 — Round Values
All numeric outputs must be **2 decimal places**:
`ROUND(value, 2)`

---

### Step 4 — SLA Status
We check ALL conditions together:
`CASE WHEN all conditions satisfied THEN 'PASS' ELSE 'FAIL' END`

---

### Step 5 — Violated SLAs
We build a string dynamically:
- Append SLA name if violated
- Concatenate using `||`
- Remove trailing comma using `RTRIM`

Example:
`CASE WHEN p95 > 400 THEN 'p95,' ELSE '' END`

---

## Final SQL Query

```sql
WITH metrics AS (
    SELECT
        endpoint,
        ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY latency_ms), 2) AS p50_ms,
        ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY latency_ms), 2) AS p95_ms,
        ROUND(PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY latency_ms), 2) AS p99_ms,
        ROUND(COUNT(*) FILTER (WHERE is_error = true) * 100.0 / COUNT(*), 2) AS error_rate_pct
    FROM api_logs
    GROUP BY endpoint
)
SELECT
    endpoint,
    p50_ms,
    p95_ms,
    p99_ms,
    error_rate_pct,
    CASE
        WHEN p50_ms <= 50
         AND p95_ms <= 400
         AND p99_ms <= 1000
         AND error_rate_pct <= 1.0
        THEN 'PASS'
        ELSE 'FAIL'
    END AS sla_status,
    RTRIM(
        CASE WHEN p50_ms > 50 THEN 'p50,' ELSE '' END ||
        CASE WHEN p95_ms > 400 THEN 'p95,' ELSE '' END ||
        CASE WHEN p99_ms > 1000 THEN 'p99,' ELSE '' END ||
        CASE WHEN error_rate_pct > 1.0 THEN 'error_rate,' ELSE '' END,
        ','
    ) AS violated_slas
FROM metrics
ORDER BY endpoint;ø

