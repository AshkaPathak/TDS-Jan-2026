# GA3 — Q9: PDF Text Bounding Box Detection

## Problem Summary

A single-page PDF is generated uniquely for each student. The PDF contains the word **"text"** placed at **10 random locations**. The task is to programmatically extract the bounding box coordinates for every occurrence and submit them as a JSON array.

Requirements:
- Find all 10 occurrences of the word `text`
- Output bounding boxes in PyMuPDF coordinate system (origin at top-left)
- Each bounding box must be `[x0, y0, x1, y1]` as integers
- Submit a valid JSON array (flat list of 10 boxes)

---

## Setup

### Step 1 — Create and activate a virtual environment (macOS Homebrew PEP 668 safe)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 2 — Install PyMuPDF

```bash
python -m pip install --upgrade pip
python -m pip install pymupdf
```

### Step 3 — Confirm installation

```bash
python -c "import fitz; print('OK')"
```

---

## Solution Approach

PyMuPDF provides `page.search_for("text")`, which returns a list of rectangles (`Rect`) for each match.

Each rectangle contains:
- `x0, y0` = top-left
- `x1, y1` = bottom-right

These are already in the required coordinate system (top-left origin). The rectangles were converted to integers and printed as strict JSON.

---

## Code (main.py)

```python
import json
import sys
import fitz  # PyMuPDF


def extract_bboxes(pdf_path: str, needle: str):
    doc = fitz.open(pdf_path)
    page = doc[0]  # single-page PDF

    rects = page.search_for(needle)

    out = []
    for r in rects:
        out.append([int(round(r.x0)), int(round(r.y0)), int(round(r.x1)), int(round(r.y1))])

    return out


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_path> <text>", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    needle = sys.argv[2]

    bboxes = extract_bboxes(pdf_path, needle)

    # Print strict JSON array as required by portal
    print(json.dumps(bboxes))


if __name__ == "__main__":
    main()
```

---

## Run Command

```bash
python main.py bounding_box_task.pdf text
```

---

## Final Output Submitted

```json
[[66, 617, 89, 637], [411, 510, 433, 530], [104, 65, 126, 84], [223, 214, 245, 233], [512, 123, 535, 142], [209, 102, 231, 121], [257, 327, 279, 346], [355, 608, 377, 627], [71, 248, 94, 267], [86, 457, 109, 476]]
```

---

## GitHub Steps

```bash
cd ~/TDS-Jan-2026

# Ensure only required files are committed (avoid venv)
echo ".venv/" >> .gitignore

git add .gitignore
git add GA3/q09_pdf_text_bounding_box_detection/main.py
git add GA3/q09_pdf_text_bounding_box_detection/q09_pdf_text_bounding_box_detection.md

git commit -m "GA3 Q9: extract PDF text bounding boxes using PyMuPDF"
git push
```

---

## Conclusion

Using PyMuPDF `page.search_for()` allowed reliable extraction of all 10 bounding boxes for the word `text` in the personalized PDF. The output was produced as a strict JSON array and successfully accepted by the portal.
