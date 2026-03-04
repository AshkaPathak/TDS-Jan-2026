# GA4 — Q13: Shell Extract and Flatten Nested JSON from Multiple Files

## Problem Summary
You are given a ZIP archive containing 50+ JSON files downloaded from an API. Each JSON file contains multiple user records with nested objects. Inside each record, there is a deeply nested field:

metrics.level

The task is to extract this field from every record across all JSON files and compute how many records exist for each level value.

The final output must follow this format:

level1:count|level2:count|...

Requirements:
- Extract all JSON files from the ZIP archive
- Use `jq` to read nested JSON fields
- Count how many records belong to each level
- Levels range from **1 to 10**
- Output must be **sorted numerically by level**
- Output must be **a single pipe-separated line**

---

## Input File
api_data_23f3002663@ds.study.iitm.ac.in.zip

---

## Strategy

The task can be solved using standard shell utilities.

1. Extract the ZIP archive containing the JSON files.
2. Use `find` to list all JSON files.
3. Use `jq` to extract `.metrics.level` from every record.
4. Sort the levels numerically.
5. Use `uniq -c` to count how many times each level appears.
6. Format the results as `levelX:count`.
7. Join the lines into a single pipe-separated string.

---

## Shell Pipeline Solution

Run the following commands in the directory containing the ZIP file.

### Step 1 — Extract JSON files
```bash
unzip -q api_data_23f3002663@ds.study.iitm.ac.in.zip -d api_data
```

### Step 2 — Extract and aggregate levels
```bash
find api_data -name '*.json' -print0 \
| xargs -0 jq -r '.[] | .metrics.level' \
| sort -n \
| uniq -c \
| awk '{print "level"$2":"$1}' \
| paste -sd'|' -
```

Explanation of each stage:

- `find api_data -name '*.json'`  
  Finds all JSON files in the extracted directory.

- `jq -r '.[] | .metrics.level'`  
  Extracts the nested `metrics.level` field from every record.

- `sort -n`  
  Sorts level values numerically.

- `uniq -c`  
  Counts occurrences of each level.

- `awk '{print "level"$2":"$1}'`  
  Formats output as `levelX:count`.

- `paste -sd'|' -`  
  Joins lines into a single pipe-separated output.

---

## Final Output

level1:47|level2:46|level3:53|level4:47|level5:45|level6:52|level7:35|level8:37|level9:44|level10:42

This satisfies all requirements:
- Sorted by level
- Correct counts
- Pipe-separated single line format

---
