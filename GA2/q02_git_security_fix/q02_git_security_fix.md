# GA2 — Q2: Git Security Fix — Removing `.env` from History

## Problem Summary

A `.env` file containing sensitive credentials was accidentally committed to a Git repository.

The task was to:

1. Identify the commit that introduced `.env`
2. Remove `.env` from the entire Git history (not just the latest commit)
3. Ensure `.env` cannot be committed again
4. Provide a safe `.env.example` file
5. Push the cleaned repository to GitHub

This required rewriting Git history, not simply deleting a file.

---

## Step 1: Identify the Commit That Added `.env`

To determine when `.env` was introduced:

```bash
git log -- .env
git log --all --full-history -- .env
```

This revealed the commit that added the `.env` file.

---

## Step 2: Remove `.env` from Entire History

Since deleting the file in a later commit does not remove it from history, `git filter-repo` was used to rewrite the entire commit history.

Because the repository was extracted from a ZIP (not a fresh clone), `--force` was required:

```bash
git filter-repo --force --path .env --invert-paths
```

This removed `.env` from all commits across all branches.

---

## Step 3: Verify Complete Removal

To ensure `.env` was fully removed:

```bash
git log --all -- .env
find . -name ".env" -print
```

Both commands returned no output, confirming:

- `.env` no longer exists in history
- `.env` is not present in the working tree

---

## Step 4: Prevent Future Secret Leaks

### Add `.env` to `.gitignore`

```bash
echo ".env" >> .gitignore
sort -u .gitignore -o .gitignore
```

### Create `.env.example`

A safe template file was added:

```bash
cat > .env.example <<'EOF'
API_KEY=your_api_key_here
DB_URL=your_database_url_here
EOF
```

This allows developers to configure local environments without committing secrets.

---

## Step 5: Commit and Force Push

After rewriting history, commit hashes change. Therefore, a force push is required.

```bash
git add .gitignore .env.example
git commit -m "Security fix: remove .env from history and add .env.example"
git push -u --force origin main
```

(If the branch name is `master`, replace `main` accordingly.)

---

## Why Force Push Was Necessary

Rewriting history modifies commit hashes.  
The remote repository must be overwritten to reflect the cleaned history.

Without a force push, GitHub would retain the old commits containing `.env`.

---

## Final Result

- `.env` removed from the entire Git history
- No secrets remain in past commits
- `.gitignore` prevents future `.env` commits
- `.env.example` provides safe configuration guidance
- Clean repository pushed to GitHub

---

## Final Repository

Cleaned repository with `.env` fully removed from history:

https://github.com/AshkaPathak/q-git-revert-env

