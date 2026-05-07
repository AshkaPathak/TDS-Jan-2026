# GA3 — Q9: PDF Text Bounding Box Detection

This README summarizes the question folder. The detailed solution remains in `q09_pdf_text_bounding_box_detection.md`.

## Method

Extracted structured information from PDF content and verified page/text/coordinate requirements.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `main.py` | Python API/service code |
| `q09_pdf_text_bounding_box_detection.md` | Detailed question writeup |

## Run or Reproduce

```bash
uvicorn main:app --host 0.0.0.0 --port 7860
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
