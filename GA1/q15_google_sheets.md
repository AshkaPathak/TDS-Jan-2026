# GA1 — Q15: Google Sheets Formula Evaluation

## Problem Summary
The task required evaluating a Google Sheets formula using dynamic array functions. The formula does not work in Excel and is specific to Google Sheets functionality.

## Given Formula

```excel
=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 15, 10), 1, 10))
```

## Function Breakdown

### 1. SEQUENCE(rows, columns, start, step)
Generates a grid of numbers.
- 100 rows
- 100 columns
- Starting at 15
- Incrementing by 10

### 2. ARRAY_CONSTRAIN(array, rows, columns)
Restricts the generated array to:
- First 1 row
- First 10 columns

### 3. SUM(...)
Adds the constrained values.

## Execution Logic
The first 10 values generated are:

15, 25, 35, 45, 55, 65, 75, 85, 95, 105

Summing them:

15 + 25 + 35 + 45 + 55 + 65 + 75 + 85 + 95 + 105 = 600

## Final Result

```
600
```

## Notes
- This formula works in Google Sheets.
- It does not work in Excel.
- Demonstrates use of dynamic array functions.

## Result
PASS
