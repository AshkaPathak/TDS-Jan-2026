# GA8 — Q5: Docker Multi-stage Build — Train and Verify an ML Model

This README summarizes the question folder. The detailed solution remains in `q05_docker_multistage.md`.

## Method

Packaged the solution with Docker and documented build/run behavior for reproducibility.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `Dockerfile` | Docker deployment |
| `compute.py` | question writeup and supporting files |
| `q05_docker_multistage.md` | Detailed question writeup |

## Run or Reproduce

```bash
docker build -t tds-question .
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
