# GA2 — Q6: Create a GitHub Action

## Problem Summary

Create a GitHub Action in a public GitHub repository such that:

- One step in the workflow has a name that contains my IITM email.
- The workflow runs successfully.
- It is the most recent workflow run.
- Submit the repository URL in the format:

```
https://github.com/<user>/<repo>
```

---

## Repository Used

**Repository Name:**  
TDS-Jan-2026  

**Repository URL:**  
https://github.com/AshkaPathak/TDS-Jan-2026  

The repository is public.

---

## Key Requirement

GitHub only detects workflow files placed inside:

```
.github/workflows/
```

If the workflow file is placed inside `GA2/` or any other subdirectory, the action will not run.

Therefore, the workflow was created inside:

```
.github/workflows/ga2_q6.yml
```

---

## Workflow File

**Path:**

```
.github/workflows/ga2_q6.yml
```

**Contents:**

```yaml
name: GA2 Q6 Action

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: 23f3002663@ds.study.iitm.ac.in
        run: echo "GA2 Q6 workflow running"
```

The required IITM email appears exactly in the step name.

---

## Triggering the Workflow

The workflow triggers automatically on every push to the `main` branch.

After pushing the workflow file:

1. Opened **GitHub → Actions tab**
2. Confirmed:
   - Workflow executed successfully (green check)
   - It is the most recent run
   - Step name includes the required email

---

## GitHub Commands Used

```bash
cd ~/TDS-Jan-2026

mkdir -p .github/workflows

nano .github/workflows/ga2_q6.yml

git add .github/workflows/ga2_q6.yml
git commit -m "Add GA2 Q6 GitHub Action"
git push
```

If re-triggering was required:

```bash
echo "trigger q6" >> trigger.txt
git add .
git commit -m "Trigger GA2 Q6 workflow"
git push
```

---

## Verification

Checked under:

GitHub → Actions

Confirmed:

✔ Workflow exists  
✔ Workflow ran successfully  
✔ Step name contains IITM email  
✔ Latest run corresponds to GA2 Q6  

---

## Final Submission

Submitted repository URL:

```
https://github.com/AshkaPathak/TDS-Jan-2026
```
