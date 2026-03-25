# GA6 — Q6: The Slice Detective

## Problem Summary

A sentiment classifier was deployed to label social media posts.

- Overall accuracy: 84.8%
- However, hidden failure modes may exist in specific subgroups (slices)

The task is to:

Find the single worst-performing slice based on accuracy.

---

## Key Idea

A slice is defined as:

- A single metadata column (platform, language_detected, message_length_bucket), OR
- A combination of two metadata columns

We must:

1. Compute accuracy for each slice
2. Only include slices with at least 42 rows
3. Compare slice accuracy with overall accuracy
4. Keep slices that are at least 5.1 percentage points worse
5. Return the slice with the lowest accuracy

---

## Accuracy Definition

Accuracy = fraction of rows where:

true_label = predicted_label

Implemented as:

CASE WHEN true_label = predicted_label THEN 1 ELSE 0 END

---

## Approach

### Step 1 — Compute overall accuracy

Using a CTE:

```sql
SELECT AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END)
```

---

### Step 2 — Generate all slices

We compute:

- Single column slices:
  - platform
  - language_detected
  - message_length_bucket

- Two-column combinations:
  - platform + language_detected
  - platform + message_length_bucket
  - language_detected + message_length_bucket

All combined using UNION ALL

---

### Step 3 — Filter valid slices

Using:

```sql
HAVING COUNT(*) >= 42
```

---

### Step 4 — Apply accuracy drop condition

The slice must be at least 5.1 percentage points below overall accuracy:

```sql
slice_accuracy <= overall_accuracy - 0.051
```

---

### Step 5 — Select worst slice

```sql
ORDER BY slice_accuracy ASC
LIMIT 1
```

---

## Final Query

```sql
WITH overall AS (
  SELECT AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END) AS overall_accuracy
  FROM predictions
),
all_slices AS (
  SELECT
    'platform = ' || platform AS slice_definition,
    COUNT(*) AS slice_size,
    AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END) AS slice_accuracy
  FROM predictions
  GROUP BY platform
  HAVING COUNT(*) >= 42

  UNION ALL

  SELECT
    'language_detected = ' || language_detected AS slice_definition,
    COUNT(*) AS slice_size,
    AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END) AS slice_accuracy
  FROM predictions
  GROUP BY language_detected
  HAVING COUNT(*) >= 42

  UNION ALL

  SELECT
    'message_length_bucket = ' || message_length_bucket AS slice_definition,
    COUNT(*) AS slice_size,
    AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END) AS slice_accuracy
  FROM predictions
  GROUP BY message_length_bucket
  HAVING COUNT(*) >= 42

  UNION ALL

  SELECT
    'platform = ' || platform || ', language_detected = ' || language_detected AS slice_definition,
    COUNT(*) AS slice_size,
    AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END) AS slice_accuracy
  FROM predictions
  GROUP BY platform, language_detected
  HAVING COUNT(*) >= 42

  UNION ALL

  SELECT
    'platform = ' || platform || ', message_length_bucket = ' || message_length_bucket AS slice_definition,
    COUNT(*) AS slice_size,
    AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END) AS slice_accuracy
  FROM predictions
  GROUP BY platform, message_length_bucket
  HAVING COUNT(*) >= 42

  UNION ALL

  SELECT
    'language_detected = ' || language_detected || ', message_length_bucket = ' || message_length_bucket AS slice_definition,
    COUNT(*) AS slice_size,
    AVG(CASE WHEN true_label = predicted_label THEN 1.0 ELSE 0.0 END) AS slice_accuracy
  FROM predictions
  GROUP BY language_detected, message_length_bucket
  HAVING COUNT(*) >= 42
)
SELECT
  s.slice_definition,
  s.slice_size,
  s.slice_accuracy,
  o.overall_accuracy
FROM all_slices s
CROSS JOIN overall o
WHERE s.slice_accuracy <= o.overall_accuracy - 0.051
ORDER BY s.slice_accuracy ASC
LIMIT 1;
```

---

## Why This Works

- Exhaustively evaluates all valid slices
- Uses HAVING to enforce minimum size constraint
- Uses UNION ALL to combine slice definitions
- Uses CROSS JOIN to attach overall accuracy
- Correctly applies percentage point threshold (0.051)
- Returns exactly one worst-performing slice

---

## Conclusion

The solution identifies hidden failure modes by:

- Breaking performance across meaningful slices
- Comparing against global performance
- Selecting the most underperforming segment

✔ Fully satisfies constraints  
✔ Returns exactly one row  
✔ Matches required output format  

Final result: Worst-performing slice identified correctly
