# GA1 — Q11: Reorganize Files by Category and Verify SHA256

## Problem Summary

A ZIP archive contained files in nested directories with edge cases:
- spaces in paths (e.g., `part 2`, `spaces here`)
- Unicode characters in folders and filenames (e.g., `naïve`, `módulo-3`, `données`, and non-ASCII letters)

Task requirements:
1. Extract the archive correctly.
2. For each `.txt` file, extract the category from the **first** line matching:

```
category: ...
```

3. Move each file to the target format:

```
{category}/{path-with-dashes}-{filename}
```

Where `path-with-dashes` is the original relative directory path with `/` replaced by `-`.

4. Compute the SHA256 hash (with consistent ordering using `LC_ALL=C sort`) and submit the required hash.

---

## Approach / Methodology

### 1) Extraction on macOS
`unzip` failed due to filename encoding (`Illegal byte sequence`). Used macOS-native extraction:

```bash
ditto -x -k ~/Downloads/files_to_reorganize.zip .
```

This extracted all files without decoding errors.

### 2) Category extraction rule
Each `.txt` file contained a category line like:

```
category: templates
```

The task required using the **first** matching `category: ...` line.

### 3) Reorganization rule
For a file originally at:

```
docs/2024/naïve/file01.txt
```

With category `configs`, the destination becomes:

```
configs/docs-2024-naïve-file01.txt
```

This flattens the directory path into dash-separated form while keeping the original filename.

### 4) Hash verification
The portal accepted the hash computed over `.txt` files with deterministic ordering:

```bash
find . -type f -name '*.txt' | LC_ALL=C sort | sha256sum
```

---

## Final Hash

Command:

```bash
find . -type f -name '*.txt' | LC_ALL=C sort | sha256sum
```

Output:

```
a28911042ec7cf553b339413d5b3ba9e1635973ec89974e3e7ea0fadab988097  -
```

Submitted hash (hex only):

`a28911042ec7cf553b339413d5b3ba9e1635973ec89974e3e7ea0fadab988097`

---

## Result
PASS
