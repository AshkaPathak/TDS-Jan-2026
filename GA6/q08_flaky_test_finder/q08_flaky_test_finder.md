# GA6 — Q8: The Flaky Test Finder

## Problem Summary

A CI system records test outcomes across many runs and commits.

A test is considered flaky only if, on the same commit, it both:

- passes in some runs
- fails in some runs

A test that always fails on one commit and always passes on another is not flaky, because its behaviour is still deterministic per commit.

The task is to return one row per flaky test with these exact columns:

- `test_name`
- `flaky_commits`
- `pass_rate`
- `flakyness_score`

where:

- `flaky_commits` = number of commits where that test had both PASS and FAIL outcomes
- `pass_rate` = fraction of all runs for that test that passed
- `flakyness_score` = `flaky_commits / total_distinct_commits_this_test_ran_on`

The output must be ordered by `flakyness_score DESC`.

---

## Key Idea

This is a two-level aggregation problem.

### Level 1 — Per `(test_name, commit_hash)`
For each test on each commit, count:

- how many PASS runs occurred
- how many FAIL runs occurred

If both counts are greater than 0, then that commit is flaky for that test.

### Level 2 — Per `test_name`
Aggregate over all commits for that test to compute:

- how many commits were flaky
- how many distinct commits this test ran on

Then compute:

- `flakyness_score = flaky_commits / total_distinct_commits_this_test_ran_on`

Separately, compute pass rate across all runs of the test.

---

## Approach

### Step 1 — Detect mixed outcomes per commit

Group by:

- `test_name`
- `commit_hash`

Then count:

- `PASS`
- `FAIL`

A commit is flaky for that test if:

- `pass_count > 0`
- `fail_count > 0`

---

### Step 2 — Aggregate flaky commits per test

For each test:

- count how many commits were flaky
- count how many distinct commits it ran on

---

### Step 3 — Compute pass rate

Across all runs of each test:

- `PASS = 1`
- `FAIL = 0`

Then take the average and round to 4 decimal places.

---

### Step 4 — Compute flakyness score

Use:

```sql
flaky_commits / total_distinct_commits_this_test_ran_on
```

Round to 4 decimal places.

Important: the grader requires the exact column name:

```sql
flakyness_score
```

with a `y`, not `flakiness_score`.

---

## Final Query

```sql
WITH commit_outcomes AS (
  SELECT
    test_name,
    commit_hash,
    COUNT(*) FILTER (WHERE outcome = 'PASS') AS pass_count,
    COUNT(*) FILTER (WHERE outcome = 'FAIL') AS fail_count
  FROM test_runs
  GROUP BY test_name, commit_hash
),
test_stats AS (
  SELECT
    test_name,
    COUNT(*) FILTER (WHERE pass_count > 0 AND fail_count > 0) AS flaky_commits,
    COUNT(*) AS total_distinct_commits_this_test_ran_on
  FROM commit_outcomes
  GROUP BY test_name
),
pass_rates AS (
  SELECT
    test_name,
    ROUND(AVG(CASE WHEN outcome = 'PASS' THEN 1.0 ELSE 0.0 END), 4) AS pass_rate
  FROM test_runs
  GROUP BY test_name
)
SELECT
  ts.test_name,
  ts.flaky_commits,
  pr.pass_rate,
  ROUND(ts.flaky_commits * 1.0 / ts.total_distinct_commits_this_test_ran_on, 4) AS flakyness_score
FROM test_stats ts
JOIN pass_rates pr
  ON ts.test_name = pr.test_name
WHERE ts.flaky_commits > 0
ORDER BY flakyness_score DESC, ts.test_name ASC;
```

---

## Why This Works

- Correctly distinguishes true flakiness from commit-to-commit behaviour changes
- Uses per-commit aggregation first, which is the core requirement
- Computes flaky commit count exactly
- Computes pass rate over all runs, as required
- Uses the exact grader-required column name `flakyness_score`
- Excludes non-flaky tests with `WHERE ts.flaky_commits > 0`

---

## Conclusion

The solution identifies flaky tests by:

- checking whether the same commit produced both PASS and FAIL
- counting how many commits showed this behaviour
- normalising by total distinct commits for each test
- reporting overall pass rate for additional context

This matches the task definition precisely and returns the required flaky test summary.

✔ True flakiness detected correctly  
✔ Two-level aggregation used properly  
✔ Exact required columns returned  
✔ Correct ordering applied
