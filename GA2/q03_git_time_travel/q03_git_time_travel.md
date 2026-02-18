# GA2 — Q3: Git Time Travel — History Investigation

## Problem Summary

A production incident was caused by a configuration change.  
The task was to identify **the commit where `config.json` changed the timeout value to `150`**, then report the **7-character short hash of the parent commit** of that change.

---

## Step 1: Inspect the Commit History for `config.json`

List commits that touched `config.json`:

```bash
git log -- config.json
```

This provides candidate commits, but does not directly show which one introduced `timeout = 150`.

---

## Step 2: Search for the Exact Change That Introduced `"timeout": 150`

Use Git’s string-introduction search (`-S`) to locate the commit where `"timeout": 150` appeared in the file:

```bash
git log -S '"timeout": 150' -p -- config.json
```

This returns commits where the string `"timeout": 150` was added or removed.

From the diff output, the commit that **sets** timeout to `150` is:

- Commit: `a34c7d87c32b523e510b0be7ca8408a6900acac4`
- Diff includes: `+    "timeout": 150,`

---

## Step 3: Get the Parent Commit of That Commit

To get the parent commit hash:

```bash
git rev-parse a34c7d87c32b523e510b0be7ca8408a6900acac4^
```

---

## Step 4: Output the 7-Character Short Hash (Final Answer)

The required answer is the parent commit’s **7-character short hash**:

```bash
git rev-parse --short a34c7d87c32b523e510b0be7ca8408a6900acac4^
```

The output of this command is the value 9069b32.
