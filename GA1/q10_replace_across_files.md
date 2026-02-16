# GA1 — Q10: Replace Across Files (Shell Commands)

## Problem Summary

We were given a ZIP file containing multiple files and instructed to:

- Extract it into a new folder
- Replace all occurrences of "IITM" (case-insensitive) with "IIT Madras"
- Leave file endings unchanged
- Then compute:

    cat * | sha256sum

The resulting SHA256 hash needed to match the expected value.

---

## Approach

1. Extracted the ZIP file into a new folder.
2. Used bulk replace to substitute all variations of:
   - IITM
   - iitm
   - Iitm
   - etc.

   With:
   - IIT Madras

3. Ensured:
   - No file extensions were changed
   - No unintended replacements occurred
   - All files were modified correctly

4. Ran the validation command:

```bash
cat * | sha256sum
```

---

## Result

```
5cb90d6ff69b9eced9363f45466fb1d80520d616897ebfe9a647eb35636dd366 -
```

The computed hash matched the expected value.

---

## Key Learnings

- Bulk replace must be done carefully (case-insensitive).
- Always verify results using hash checks.
- Command-line tools are powerful for validation.
- Never change file endings unless explicitly instructed.

---

## Result
PASS
