# GA6 — Q12: The Idempotency Prober

## Problem Summary

You are given a dataset with numerical and categorical columns. A preprocessing function `f(x)` is applied to clean the data:

1. Clip all numeric columns to the range [0, 100]  
2. Forward-fill missing values  
3. Replace any remaining missing values with 0  

You must evaluate whether this preprocessing pipeline satisfies three important invariants:

1. Idempotency  
2. Monotonicity  
3. Null Stability  

---

## Definitions

### 1. Idempotency

A function is idempotent if:

f(f(x)) = f(x)

For each row, apply the preprocessing function twice and compare with a single application. If any value differs, it is counted as an idempotency violation.

---

### 2. Monotonicity

For all pairs (i, j):

If original value_a[i] > value_a[j], then the processed output must also satisfy:

processed_value_a[i] > processed_value_a[j]

If this ordering is not preserved, it is a monotonicity violation.

Only pairs where original values are strictly ordered are considered.

---

### 3. Null Stability

If a row originally has no missing values, the processed row should also have no missing values.

If new nulls are introduced, it is a null stability violation.

---

## Approach

1. Apply preprocessing once → processed1  
2. Apply preprocessing again → processed2  
3. Compare processed1 and processed2 for idempotency  
4. Compare all valid ordered pairs for monotonicity  
5. Check for newly introduced null values  

---

## Final Answer

0,121,0

Where:
- idempotency_violations = 0  
- monotonicity_violations = 121  
- null_stability_violations = 0  

---

## Why This Works

- Clipping and forward-filling are stable operations, so idempotency holds  
- However, clipping compresses values (e.g., values above 100 become equal), which can break strict ordering → monotonicity violations  
- Forward fill and zero fill do not introduce new nulls → null stability holds  
