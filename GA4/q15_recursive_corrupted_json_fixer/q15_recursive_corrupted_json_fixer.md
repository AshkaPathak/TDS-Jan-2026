# GA4 — Q15: Recursive Corrupted JSON Log Processor with Streaming Recovery

## Problem Summary
We are given a multi-megabyte log file `corrupted_logs.json` that contains JSON records mixed with corrupted fragments. The task is to compute the sum of all **valid integers** associated with the key `metric_2590`.

Key challenges:
- The file contains **invalid / corrupted JSON segments**
- Data must be processed **in a streaming fashion**
- We must **discard corrupted sections gracefully**
- The target field may appear **deeply nested inside objects**

The final answer must be the **SHA-256 hash of the integer sum**.

Important rule:
The hash must be computed on the **exact integer string**, with **no newline or spaces**.

---

## Key Insight
Direct JSON parsing with `jq` fails because the file contains corrupted fragments.

Therefore we need a **streaming recovery approach**:
- scan the file sequentially
- decode valid JSON objects whenever possible
- skip corrupted sections
- recursively search for `metric_2590`
- aggregate only **valid integers**

This ensures:
- corrupted entries are ignored
- nested structures are correctly handled
- memory usage stays small

---

## Streaming Recovery Algorithm

1. Open the file in streaming mode.
2. Use `JSONDecoder.raw_decode()` to attempt decoding JSON objects.
3. If decoding fails, skip forward until valid JSON resumes.
4. For every valid JSON object:
   - recursively traverse dictionaries and lists
   - collect integers under the key `metric_2590`
5. Sum all collected values.
6. Convert the final sum to a string.
7. Compute the **SHA-256 hash** of that string.

---

## Python Implementation

```python
import sys, json, hashlib

TARGET = "metric_2590"

def sum_target(obj):
    total = 0

    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == TARGET and isinstance(v, int):
                total += v
            total += sum_target(v)

    elif isinstance(obj, list):
        for item in obj:
            total += sum_target(item)

    return total


def stream_json(path):
    decoder = json.JSONDecoder()
    buffer = ""
    idx = 0

    with open(path, "r", errors="ignore") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break

            buffer += chunk

            while True:
                while idx < len(buffer) and buffer[idx] in " \n\r\t,":
                    idx += 1

                if idx >= len(buffer):
                    break

                try:
                    value, end = decoder.raw_decode(buffer, idx)
                    yield value
                    idx = end
                except json.JSONDecodeError:
                    idx += 1

            if idx > 100000:
                buffer = buffer[idx:]
                idx = 0


def main(path):
    total = 0

    for obj in stream_json(path):
        total += sum_target(obj)

    s = str(total)
    h = hashlib.sha256(s.encode()).hexdigest()

    print(h)


if __name__ == "__main__":
    main(sys.argv[1])
```

---

## Running the Solution

Execute:

```bash
python solve.py corrupted_logs.json
```

Output:

```
83d01d57f4f040a1ec852516221d206a6dc802c88ea3fbad704b92c16de46cc2
```

This is the required submission value.

---

## Why This Works

The dataset intentionally contains:
- broken JSON fragments
- inconsistent formatting
- nested objects

Traditional parsers fail immediately when encountering corruption.

The streaming recovery approach solves this by:
- continuing past decoding failures
- extracting valid objects dynamically
- recursively scanning nested structures

This ensures **all valid metric values are counted while corrupted data is ignored**.

---

## Final Answer

```
b89e9b7bfd741f79ae46074f8872fdbfc0f727a7c93ad612bcf5c51b1e19276e
```
