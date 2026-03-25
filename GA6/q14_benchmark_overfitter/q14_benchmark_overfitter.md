# GA6 — Q14: Benchmark Overfitter

## Problem Summary
A team evaluates multiple model configurations repeatedly on the **same fixed test set** and selects the best result. This leads to **benchmark overfitting**, where reported accuracy is inflated.

We must compute:
- Standard deviation of accuracy estimates (sigma)
- Expected inflation (in percentage points)
- Adjusted accuracy after removing inflation

---

## Given

- Evaluation rounds: T = 100  
- Test set size: n_test = 5000  
- Reported accuracy: p = 0.8500  

---

## Step-by-Step Solution

### Step 1 — Compute Sigma

For a binomial proportion:

σ = sqrt(p(1 − p) / n_test)

Substituting values:

σ = sqrt(0.8500 × 0.1500 / 5000)  
σ = sqrt(0.1275 / 5000)  
σ = sqrt(0.0000255)  
σ ≈ 0.005050  

(rounded to 6 decimal places)

---

### Step 2 — Compute Expected Inflation

Formula:

inflation = σ × sqrt(2 ln(T))

Compute ln(T):

ln(100) ≈ 4.60517  

Compute:

sqrt(2 × 4.60517) = sqrt(9.21034) ≈ 3.034  

Now:

inflation = 0.005050 × 3.034 ≈ 0.01533  

Convert to percentage points:

0.01533 × 100 = 1.533  

(rounded to 3 decimal places)

---

### Step 3 — Compute Adjusted Accuracy

Reported accuracy:

0.8500 × 100 = 85.000  

Adjusted accuracy:

85.000 − 1.533 = 83.467  

(rounded to 3 decimal places)

---

## Final Answer

0.005050, 1.533, 83.467

---

## Key Insights

- Repeated evaluation on the same test set inflates performance.
- Inflation grows with number of trials (T).
- Tail risk is captured using sqrt(2 ln T).
- Adjusted accuracy gives a more realistic estimate.

---

## Conclusion

This problem demonstrates how statistical variance and repeated selection bias can lead to overly optimistic performance estimates, and how to correct for it using probabilistic bounds.
