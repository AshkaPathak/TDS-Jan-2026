# GA8 — Q1: GitHub Actions Secret Hash Chain

## Problem Summary
This question required creating a GitHub Actions workflow that securely reads a repository secret and generates a verifiable hash. The workflow had to compute the SHA-256 hash of `MY_SECRET + "github-verified"`, take the first 10 characters, upload the result as an artifact, and submit the successful workflow run URL together with the generated hash.

## Secret Setup
A GitHub repository secret was added with the exact required name and value:

- Secret name: `MY_SECRET`
- Secret value: `a3e192014453`

This was added through:
GitHub Repository → Settings → Secrets and variables → Actions → New repository secret

## Important Requirement
The workflow file must be placed at the repository root path:
.github/workflows/hash-chain.yml

Placing the workflow inside any subfolder like GA8/q01_secret_hash_chain/.github/workflows/ will NOT work because GitHub only detects workflows from the root .github/workflows directory.

## Final Workflow
```yaml
name: Secret Hash Chain

on:
  push:
  workflow_dispatch:

jobs:
  verify:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Compute hash afbc3d62
        run: |
          echo -n "${MY_SECRET}github-verified" | sha256sum | cut -c1-10 > verify_hash.txt
        env:
          MY_SECRET: ${{ secrets.MY_SECRET }}

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: verify-hash-afbc3d62
          path: verify_hash.txt
```

## Why This Works
This satisfies all checker requirements:
- Uses secrets.MY_SECRET correctly
- Includes the string "github-verified"
- Uses sha256sum for hashing
- Includes marker afbc3d62 in step name
- Uploads artifact verify-hash-afbc3d62
- Produces a non-empty verify_hash.txt
- Supports both push and workflow_dispatch triggers

## Hash Generation Logic
The core command used was:
echo -n "${MY_SECRET}github-verified" | sha256sum | cut -c1-10 > verify_hash.txt

Explanation:
- echo -n prevents newline addition (critical for correct hash)
- Concatenates MY_SECRET with "github-verified"
- sha256sum computes hash
- cut extracts first 10 characters
- Output saved to verify_hash.txt

## Debugging and Fixes
1. Workflow file placed in wrong directory  
Fix: moved to .github/workflows/hash-chain.yml

2. Deprecated artifact version  
Changed:
uses: actions/upload-artifact@v3  
to:
uses: actions/upload-artifact@v4

3. Incorrect submission URL  
Used job/log URL instead of run URL  
Correct format:
https://github.com/OWNER/REPO/actions/runs/RUN_ID

## Successful Output
The artifact verify_hash.txt contained:
1fe4f1a6a7

## Final Submission
https://github.com/AshkaPathak/TDS-Jan-2026/actions/runs/24742799249|1fe4f1a6a7

## Conclusion
This workflow demonstrates secure secret handling in GitHub Actions, correct workflow configuration, and deterministic hashing with artifact-based verification.
