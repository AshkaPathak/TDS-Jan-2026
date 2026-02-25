# GA3 — Q4: Scheduled GitHub Action (Daily Commit)

## Problem Summary

Create a scheduled GitHub Action that:

- Runs **once per day** using `schedule` with a valid `cron` expression
- Uses a specific hour and minute (not `* * * * *`)
- Includes the email **23f3002663@ds.study.iitm.ac.in** in the workflow/run name
- Creates a **commit** during each run
- Is placed inside `.github/workflows/`
- After creation:
  - Trigger the workflow
  - Ensure it is the **latest run**
  - Ensure it creates a commit within **5 minutes**

---

## Repository Submitted to Portal

To avoid conflicts with other workflows becoming the “latest run”,  
a clean repository containing only this workflow was used:

```
https://github.com/AshkaPathak/ga3-q4-scheduled-action
```

This repository successfully passed the portal validation.

---

## Workflow File Location

```
.github/workflows/daily-update-23f3002663.yml
```

---

## Final Workflow Implementation

```yaml
name: Daily DevSync Update - 23f3002663@ds.study.iitm.ac.in
run-name: Daily DevSync Update - 23f3002663@ds.study.iitm.ac.in

permissions:
  contents: write

on:
  schedule:
    - cron: "30 10 * * *"   # Runs once per day at 10:30 UTC
  workflow_dispatch:

jobs:
  update-repo:
    name: Update Repo - 23f3002663@ds.study.iitm.ac.in
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository - 23f3002663@ds.study.iitm.ac.in
        uses: actions/checkout@v4
        with:
          persist-credentials: true

      - name: Configure Git - 23f3002663@ds.study.iitm.ac.in
        run: |
          git config user.name "github-actions"
          git config user.email "23f3002663@ds.study.iitm.ac.in"

      - name: Create daily update file
        run: |
          echo "Last update: $(date -u)" > daily_update.txt

      - name: Commit and Push - 23f3002663@ds.study.iitm.ac.in
        run: |
          git add daily_update.txt
          git commit -m "Automated daily update - 23f3002663@ds.study.iitm.ac.in"
          git push
```

---

## Verification Steps

1. Workflow file committed and pushed to repository.
2. Workflow manually triggered using:
   - GitHub → Actions → Run workflow
3. Confirmed:
   - The **latest run name includes** `23f3002663@ds.study.iitm.ac.in`
   - A commit was created within 5 minutes:
     ```
     Automated daily update - 23f3002663@ds.study.iitm.ac.in
     ```
   - `daily_update.txt` was updated in the repository.

---

## Cron Expression Explanation

```
30 10 * * *
```

- Minute: 30
- Hour: 10 (UTC)
- Day of month: every day
- Month: every month
- Day of week: every day

This ensures the workflow runs exactly once per day.

---

## Final Submission

```
https://github.com/AshkaPathak/ga3-q4-scheduled-action
```
