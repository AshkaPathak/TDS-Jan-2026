# GA6 — Q11: Train-Test Contamination Scanner

## Problem Summary

You are given a training dataset and a test dataset. A model reports 75.75% accuracy on the test set, but there is suspicion of data leakage — some test rows may have appeared in training.

Each dataset contains the following columns:
- age
- income
- education
- hours_per_week
- label

The test set also includes:
- predicted_label
- is_correct

A test row is considered **leaked** if its feature columns (age, income, education, hours_per_week) exactly match any row in the training set. The label column is not used for matching.

---

## Task

You must compute four values:

1. leaked_count — number of leaked test rows  
2. leaked_accuracy — accuracy (is_correct rate) on leaked rows (%)  
3. clean_accuracy — accuracy on non-leaked rows (%)  
4. inflation_pp — difference between reported accuracy and clean accuracy  

---

## Approach

1. Identify leaked rows by matching feature columns between train and test datasets.
2. Separate test rows into:
   - leaked rows
   - clean (non-leaked) rows
3. Compute:
   - leaked_accuracy = (correct predictions on leaked rows / leaked_count) × 100
   - clean_accuracy = (correct predictions on clean rows / clean_count) × 100
4. Compute inflation:
   - inflation_pp = 75.75 − clean_accuracy

---

## Implementation Idea (Python)

- Load both datasets
- Perform an inner join on feature columns to identify leaked rows
- Mark test rows that appear in training
- Compute accuracy separately for leaked and clean subsets

---

## Final Answer

60,88.33,73.53,2.22

Where:
- leaked_count = 60  
- leaked_accuracy = 88.33  
- clean_accuracy = 73.53  
- inflation_pp = 2.22  

---

## Why This Matters

- Data leakage artificially inflates model performance  
- Leaked rows are easier because the model has effectively seen them before  
- Clean accuracy reflects true generalization ability  
- The difference (inflation) quantifies the impact of leakage
