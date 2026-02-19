# GA2 — Q7: Create a GitHub Action with Dependency Caching

## Problem Summary

Create a GitHub Actions workflow that speeds up CI by adding dependency caching.

Requirements:

- Create a GitHub Actions workflow in a public repository.
- Use `actions/cache@v4` (or newer).
- Prime the cache using a key named:

```
cache-e04ed7f
```

- Include a step named:

```
prime-cache-e04ed7f
```

that echoes the cache hit/miss result.
- Push the workflow and run it.
- Ensure the latest workflow run is public and successful.
- Submit the repository URL.

---

## Repository Used

**Repository Name:**  
TDS-Jan-2026  

**Repository URL:**  
https://github.com/AshkaPathak/TDS-Jan-2026  

The repository is public.

---

## Key Insight

GitHub Actions only detects workflows stored in:

```
.github/workflows/
```

So the caching workflow must be created inside that folder to run.

---

## Workflow File

**Path:**

```
.github/workflows/ga2_q7_cache.yml
```

**Contents:**

```yaml
name: GA2 Q7 Cache Action

on:
  push:
    branches:
      - main

jobs:
  cache-job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Cache dependencies
        id: cache
        uses: actions/cache@v4
        with:
          path: ~/.cache
          key: cache-e04ed7f

      - name: prime-cache-e04ed7f
        run: echo "Cache hit? ${{ steps.cache.outputs.cache-hit }}"
```

This satisfies:

- Uses `actions/cache@v4`
- Cache key is exactly `cache-e04ed7f`
- Includes a step named `prime-cache-e04ed7f`
- Prints the cache hit status from `steps.cache.outputs.cache-hit`

---

## Running and Verification

After pushing the workflow:

1. Opened **GitHub → Actions**
2. Selected **GA2 Q7 Cache Action**
3. Verified:
   - Workflow run succeeded (green check)
   - Cache step executed successfully
   - `prime-cache-e04ed7f` step printed the cache hit/miss status
   - Latest run is the GA2 Q7 workflow run

---

## GitHub Steps

```bash
cd ~/TDS-Jan-2026

# (Workflow already created earlier)
# Now add the GA2 documentation file
mkdir -p GA2/q07_dependency_caching
nano GA2/q07_dependency_caching/q07_dependency_caching.md

git add GA2/q07_dependency_caching/q07_dependency_caching.md
git commit -m "GA2 Q7: add dependency caching workflow documentation"
git push
```

---

## Final Submission

Submitted repository URL:

```
https://github.com/AshkaPathak/TDS-Jan-2026
```

---

## Conclusion

A GitHub Actions workflow was created using `actions/cache@v4` with the required cache key and step name. The workflow ran successfully, and the most recent run confirms the cache step executed and the hit/miss status was printed.

