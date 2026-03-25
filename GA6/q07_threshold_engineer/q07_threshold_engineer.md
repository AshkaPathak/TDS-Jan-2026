# GA6 — Q7: The Threshold Engineer

## Problem Summary

A content moderation classifier outputs a confidence score between 0 and 1 for whether a piece of content is harmful.

A piece of content is:

- blocked if `score >= threshold`
- shown otherwise

The business specifies that:

- a false negative costs **5×** as much as a false positive

The goal is to find the threshold from:

`{0.05, 0.10, 0.15, ..., 0.95}`

that minimises:

`expected_cost = (5 × false_negatives + false_positives) / total_rows`

The query must return exactly one row with these columns:

- `optimal_threshold`
- `precision_at_threshold`
- `recall_at_threshold`
- `expected_cost_at_threshold`

---

## Key Idea

This is a threshold selection problem under asymmetric misclassification cost.

For each candidate threshold:

- predict harmful if `score >= threshold`
- compute:
  - `TP`: predicted harmful and actually harmful
  - `FP`: predicted harmful but actually safe
  - `FN`: predicted safe but actually harmful

Then calculate:

- `precision = TP / (TP + FP)`
- `recall = TP / (TP + FN)`
- `expected_cost = (5 × FN + FP) / total_rows`

Finally, pick the threshold with the minimum expected cost.

---

## Approach

### Step 1 — Generate all candidate thresholds

DuckDB’s `generate_series(5, 95, 5)` gives:

- 5, 10, 15, ..., 95

Dividing by `100.0` converts them into:

- 0.05, 0.10, 0.15, ..., 0.95

---

### Step 2 — Evaluate every threshold against every row

Using `CROSS JOIN` between:

- thresholds
- predictions

This allows all metrics to be computed in one query.

---

### Step 3 — Compute confusion matrix metrics

For each threshold:

- `TP`: `score >= threshold AND true_label = 1`
- `FP`: `score >= threshold AND true_label = 0`
- `FN`: `score < threshold AND true_label = 1`

Also compute:

- `COUNT(*) AS total_rows`

---

### Step 4 — Compute precision, recall, and expected cost

Use:

- `ROUND(..., 4)` for precision and recall
- `ROUND(..., 6)` for expected cost

Use `NULLIF(..., 0)` to avoid divide-by-zero errors.

---

### Step 5 — Select the best threshold

Order by:

- lowest `expected_cost_at_threshold`
- then smallest threshold as tie-breaker

Return exactly one row using `LIMIT 1`.

---

## Final Query

```sql
WITH thresholds AS (
  SELECT t / 100.0 AS threshold
  FROM generate_series(5, 95, 5) AS gs(t)
),
metrics AS (
  SELECT
    t.threshold,
    SUM(CASE WHEN p.score >= t.threshold AND p.true_label = 1 THEN 1 ELSE 0 END) AS tp,
    SUM(CASE WHEN p.score >= t.threshold AND p.true_label = 0 THEN 1 ELSE 0 END) AS fp,
    SUM(CASE WHEN p.score < t.threshold AND p.true_label = 1 THEN 1 ELSE 0 END) AS fn,
    COUNT(*) AS total_rows
  FROM thresholds t
  CROSS JOIN predictions p
  GROUP BY t.threshold
),
ranked AS (
  SELECT
    threshold AS optimal_threshold,
    ROUND(tp * 1.0 / NULLIF(tp + fp, 0), 4) AS precision_at_threshold,
    ROUND(tp * 1.0 / NULLIF(tp + fn, 0), 4) AS recall_at_threshold,
    ROUND((5.0 * fn + fp) / total_rows, 6) AS expected_cost_at_threshold
  FROM metrics
)
SELECT
  optimal_threshold,
  precision_at_threshold,
  recall_at_threshold,
  expected_cost_at_threshold
FROM ranked
ORDER BY expected_cost_at_threshold ASC, optimal_threshold ASC
LIMIT 1;
```

---

## Why This Works

- Evaluates every allowed threshold
- Uses the exact business cost formula
- Correctly computes TP, FP, and FN
- Handles division safely
- Returns exactly one optimal threshold row
- Respects required rounding and output column names

---

## Conclusion

The solution converts threshold tuning into a SQL optimisation problem by:

- generating candidate thresholds
- computing classification metrics for each
- minimising expected business cost

This correctly finds the optimal operating threshold for the moderation classifier.

✔ Exact threshold grid used  
✔ Correct cost weighting applied  
✔ Required metrics returned  
✔ Exactly one row produced
