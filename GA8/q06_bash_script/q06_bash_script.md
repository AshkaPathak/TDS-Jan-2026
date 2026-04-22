# GA8 — Q6: MLOps Bash Script — Deterministic Output

## Problem Summary
The task was to write a Bash script that:

- Creates a directory named `models`
- Creates 5 empty files: `run_1.txt` through `run_5.txt`
- Computes SHA-256 hashes of each filename (not file contents)
- Takes the first 8 characters of each hash
- Concatenates these hashes in order
- Computes SHA-256 of the concatenated string and takes the first 8 characters
- Prints a summary line in the format:

DIR:models|FILES:5|HASH:{combined_hash}

---

## Step-by-Step Solution

### Step 1 — Script Implementation

The following Bash script satisfies all requirements:

```bash
#!/bin/bash

TARGET_DIR="models"
FILE_COUNT=5
HASHES=""

mkdir -p "$TARGET_DIR"

for i in $(seq 1 $FILE_COUNT); do
    fname="run_${i}.txt"
    touch "$TARGET_DIR/$fname"
    h=$(echo -n "$fname" | shasum -a 256 | cut -c1-8)
    HASHES="${HASHES}${h}"
done

COMBINED=$(echo -n "$HASHES" | shasum -a 256 | cut -c1-8)

echo "DIR:${TARGET_DIR}|FILES:${FILE_COUNT}|HASH:${COMBINED}"
```

---

## Important Details

- `echo -n` is critical to avoid adding a newline character before hashing
- `shasum -a 256` is used for macOS compatibility
- Only filenames are hashed, not file contents
- Hashes are concatenated in order: run_1 → run_5

---

## Step 2 — Run the Script

Commands used:

```bash
chmod +x script.sh
./script.sh
```

---

## Output

```text
DIR:models|FILES:5|HASH:fd9b54db
```

---

## Verification

The result matches the expected deterministic output:

- Directory created correctly
- Files created correctly
- Hash computation matches specification
- Final combined hash is correct

---

## Final Answer

DIR:models|FILES:5|HASH:fd9b54db
