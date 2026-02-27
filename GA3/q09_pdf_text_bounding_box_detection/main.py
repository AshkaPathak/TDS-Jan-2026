import json
import sys

import fitz  # PyMuPDF


def extract_bboxes(pdf_path: str, needle: str):
    doc = fitz.open(pdf_path)
    if doc.page_count < 1:
        raise ValueError("PDF has no pages")

    page = doc[0]  # single-page PDF as per problem statement

    # search_for returns list[Rect] in PyMuPDF coordinate system (origin top-left)
    rects = page.search_for(needle)

    # Convert rects -> integer [x0, y0, x1, y1]
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

    # The portal expects EXACT JSON (flat array of arrays)
    print(json.dumps(bboxes))


if __name__ == "__main__":
    main()
