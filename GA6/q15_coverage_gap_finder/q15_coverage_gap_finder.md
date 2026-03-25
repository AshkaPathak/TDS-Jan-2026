# GA6 — Q15: Coverage Gap Finder

## Problem Summary
We are given a coverage report for `processor.py` containing:
- executed_lines
- missing_lines
- branches
- total_statements
- total_branches

We must compute:
1. line_coverage_pct
2. branch_coverage_pct
3. missing_line_runs
4. critical_missing

---

## Given

- total_statements = 100  
- total_branches = 50  

- executed_lines = 60 entries  
- missing_lines = 40 entries  

---

## Step-by-Step Solution

### Step 1 — Line Coverage

Formula:

line_coverage_pct = (executed_lines / total_statements) × 100

= (60 / 100) × 100  
= 60.00  

---

### Step 2 — Branch Coverage

Count number of branches where value = true.

True branches = 23  

branch_coverage_pct = (23 / 50) × 100  
= 46.00  

---

### Step 3 — Missing Line Runs

Group consecutive missing lines:

[1], [3,4], [7,8], [13], [16], [20],  
[25,26,27], [36], [44], [48],  
[53], [55], [57,58], [61],  
[63,64,65], [74], [81],  
[85,86], [88], [90],  
[100,101,102,103], [105], [108],  
[111], [114,115], [117,118,119]

For each group:
tests required = ceil(group_size / 3)

Summing all groups:

missing_line_runs = 27  

---

### Step 4 — Critical Missing

Find largest consecutive group:

Largest group = [100,101,102,103]  
Size = 4  

critical_missing = 4  

---

## Final Answer

60.00, 46.00, 27, 4

---

## Key Insights

- Line coverage depends on executed vs total statements.
- Branch coverage depends on counting True branches.
- Missing lines must be grouped into consecutive segments.
- Each test covers at most 3 lines → use ceiling.
- Largest gap identifies the most critical missing region.

---

## Conclusion

This problem highlights how to interpret coverage reports and translate them into actionable metrics for testing strategy and code reliability.
