# GA1 — Q26: Refactor JSON to Columnar Format

## Input
The provided `data.json` contains 200 events in an array-of-objects format.

## Output Format
Converted to:
- `columns`: ordered list of all keys
- `rows`: list of value arrays aligned to the column order

Missing keys (if any) are filled with `null`.

## Implementation
Script: `to_columnar.py`
- Collect union of keys across all objects
- Use deterministic column order (sorted keys)
- Build each row with `obj.get(col, None)`
- Write output to `data_columnar.json`

## Submission
The contents of `data_columnar.json` were pasted into the portal.
