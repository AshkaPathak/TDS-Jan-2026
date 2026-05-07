# GA3 — Q11: AI Video Attendee Extraction (Gemini Files API)

This README summarizes the question folder. The detailed solution remains in `q11_ai_video_attendee_extraction_gemini.md`.

## Method

Used an LLM or prompt/API workflow with structured inputs, controlled outputs, and validation against the expected format.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `attendee_checkin_23f3002663.webm` | media artifacts |
| `main.py` | Python API/service code |
| `q11_ai_video_attendee_extraction_gemini.md` | Detailed question writeup |

## Run or Reproduce

```bash
uvicorn main:app --host 0.0.0.0 --port 7860
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
