# GA1 — Q14: Excel Formula Evaluation (Office 365)

## Problem Summary
The task required evaluating an Excel formula using Office 365 dynamic array functions. The formula involved nested use of `SORTBY`, `TAKE`, and `SUM`.

The question explicitly stated that it works only in Office 365 due to modern dynamic array support.

## Given Formula

```excel
=SUM(TAKE(SORTBY({12,6,6,7,14,8,1,8,1,13,14,2,5,0,1,15},
                 {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}),
          1, 5))
```

## Function Breakdown

### 1. SORTBY(array, by_array)
Sorts the first array based on the values of the second array.

### 2. TAKE(array, rows, columns)
Extracts the first `rows` and `columns` from the sorted result.

### 3. SUM(...)
Adds the extracted values.

## Execution Logic
1. The first array is sorted using the second array as the sorting key.
2. The first 5 elements from the sorted result are taken.
3. These 5 values are summed.

## Final Result

```
24
```

## Notes
- This formula works only in Excel Office 365.
- Older versions will return `#NAME?` because they do not support `TAKE` or `SORTBY`.

## Result
PASS
