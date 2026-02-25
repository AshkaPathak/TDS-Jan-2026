# GA3 — Q5: GitHub Actions Workflow with Status Badge (1 Mark)

## Problem Summary

Create a GitHub Actions workflow that runs successfully and display its status in the repository README using a status badge. The objective is to provide CI/CD visibility directly from the repository homepage.

---

## Repository Used

Repository created specifically for this question:

https://github.com/AshkaPathak/ga3-q05-actions-badge

The repository was kept minimal to prevent future commits from affecting workflow status.

---

## Step 1 — Create GitHub Actions Workflow

Create the workflow directory:

```bash
mkdir -p .github/workflows
```

Create the workflow file:

```bash
nano .github/workflows/ci.yml
```

Contents of `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Smoke test
        run: echo "Workflow executed successfully"
```

Explanation:

- `push` triggers workflow on every commit to `main`
- `workflow_dispatch` enables manual trigger
- `ubuntu-latest` is the runner
- A simple echo command guarantees a successful run

---

## Step 2 — Commit and Push Workflow

```bash
git add .github/workflows/ci.yml
git commit -m "Add CI workflow"
git push
```

Verification:

- Go to GitHub → Actions tab
- Confirm latest run shows a green checkmark (successful execution)

---

## Step 3 — Generate Status Badge

From GitHub:

1. Open the Actions tab
2. Click the workflow (CI)
3. Click the three dots (⋯)
4. Select "Create status badge"
5. Copy the generated Markdown

Badge Markdown used:

```markdown
![CI](https://github.com/AshkaPathak/ga3-q05-actions-badge/actions/workflows/ci.yml/badge.svg)
```

---

## Step 4 — Add Badge to README

Edit `README.md`:

```markdown
# ga3-q05-actions-badge

![CI](https://github.com/AshkaPathak/ga3-q05-actions-badge/actions/workflows/ci.yml/badge.svg)
```

Commit and push:

```bash
git add README.md
git commit -m "Add CI status badge"
git push
```

---

## Final Verification

- Workflow run shows green check
- Repository homepage displays green CI badge
- Repository is public
- Badge reflects live workflow status

---

## Final Output

Workflow file:
.github/workflows/ci.yml

Badge added to:
README.md

Submitted Repository:
https://github.com/AshkaPathak/ga3-q05-actions-badge

---

## Conclusion

A minimal GitHub Actions workflow was successfully created and verified. A live status badge was added to the repository README to provide CI visibility. The workflow runs automatically on push and can also be triggered manually.
