# GA4 — Q14: Shell Deduplicate and Aggregate Semi-Structured Address Data

## Problem Summary
We are given a large text file containing 1000+ semi-structured address lines. The data contains duplicates with small formatting variations such as: extra spaces, different capitalization, optional commas, and extra text like `Address:` prefix and `(VALID)` suffix. The task is to normalize each line to a canonical “core address”, deduplicate, and count unique addresses. Final output must be exactly: `unique_addresses:count`

## Input File
addresses_23f3002663@ds.study.iitm.ac.in.txt

## Key Insight
To correctly deduplicate, we must normalize away non-essential formatting differences. A robust canonicalization in shell is: remove the `Address:` prefix, remove `(VALID)` suffix, replace commas with spaces, lowercase everything, and collapse multiple spaces into a single space. After that, `sort -u` gives unique core addresses, and `wc -l` gives the count.

## Final Working Command
Run this in the folder containing the file:
```bash
cat "addresses_23f3002663@ds.study.iitm.ac.in.txt" \
| sed -E 's/^Address:[[:space:]]*//; s/[[:space:]]*\\(VALID\\)[[:space:]]*$//; s/,/ /g' \
| tr '[:upper:]' '[:lower:]' \
| sed -E 's/[[:space:]]+/ /g; s/^[[:space:]]+//; s/[[:space:]]+$//' \
| sort -u \
| wc -l \
| awk '{print "unique_addresses:"$1}'

## Portal Output
unique_addresses:1083
