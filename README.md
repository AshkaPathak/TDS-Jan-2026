# TDS Jan 2026 Assignment Repository

This repository is a structured archive of Tools in Data Science January 2026 assignment work. It is organized by graded assignment and by question, with README files used as navigation and method summaries.

The goal is to make every answer auditable: each question should show what was asked, what method was used, what artifact was produced, and how the result was verified.

## Assignment Map

| Folder | Questions Indexed | Main Methods Covered |
| --- | ---: | --- |
| `GA1/` | 25 | prompting, command-line work, code debugging, Git-aware file operations, spreadsheets, SQL, browser inspection, and compact data representation |
| `GA2/` | 16 | Git history, GitHub Pages, Actions, dependency automation, Codespaces, Gists, FastAPI, Docker, and Cloudflare deployment |
| `GA3/` | 18 | structured LLM outputs, FastAPI endpoints, scheduled workflows, browser automation, PDF/video/audio extraction, and web scraping |
| `GA4/` | 20 | Excel operations, dbt models, OpenRefine, JSON flattening and recovery, shell pipelines, FastAPI sentiment APIs, DuckDB, image/audio reconstruction, and entity disambiguation |
| `GA5/` | 21 | embeddings, CLIP search, topic modeling, Excel analytics, forecasting, geospatial distance calculations, DuckDB queries, moving averages, and RAG |
| `GA6/` | 15 | property-based testing, eval rubrics, robustness audits, data contracts, thresholding, flaky test analysis, leakage checks, idempotency checks, and coverage gaps |
| `GA7/` | 15 | chart critique, encoding fixes, data-narrative reconciliation, prompt repair, anomaly prioritization, poisoned-document detection, and cost/performance analysis |
| `GA8/` | 15 | secret hashing, Gemini API calls, FastAPI model services, Hugging Face Spaces, Docker multi-stage builds, Ruff CI, Cloud Run, Cloud Functions, and hash verification APIs |

## README Coverage

- Every GA folder from `GA1` to `GA8` has a README index.
- Question folders have README files that summarize the specific method and point to the detailed writeup.
- Existing preserved task text such as `original_README.md` is kept as source material rather than rewritten as project documentation.

## Repository Conventions

- Markdown writeups explain the problem, constraints, method, implementation, verification, and final answer where applicable.
- Code, data, Dockerfiles, deployment configs, Playwright scripts, generated images, and outputs stay next to the question that uses them.
- README files are navigation and audit summaries, not replacements for detailed question writeups.

## Fast Navigation

- [GA1](GA1/README.md): foundations, prompts, shell, SQL, spreadsheets, browser inspection, JSON conversion
- [GA2](GA2/README.md): GitHub, deployment, Actions, Docker, APIs, Cloudflare
- [GA3](GA3/README.md): LLM APIs, scraping, browser automation, PDF/audio/video extraction
- [GA4](GA4/README.md): data preparation, dbt, JSON recovery, shell transforms, DuckDB, entity disambiguation
- [GA5](GA5/README.md): embeddings, analytics, forecasting, geospatial computation, RAG
- [GA6](GA6/README.md): evals, quality engineering, audits, leakage and coverage checks
- [GA7](GA7/README.md): visualization critique, narrative repair, anomaly and flaw prioritization
- [GA8](GA8/README.md): MLOps, GCP, Cloud Run, Cloud Functions, Docker, Gemini APIs

## Reproducibility Intent

This repo is not just a dump of final answers. It is meant to preserve the reasoning path and the practical tool choices behind each answer, so future review can trace from question to method to artifact.
