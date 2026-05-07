# TDS Jan 2026 Assignment Archive

[![Course](https://img.shields.io/badge/course-Tools%20in%20Data%20Science-blue)](#)
[![Python](https://img.shields.io/badge/python-3.11%2B-green)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-services-teal)](#)
[![Docker](https://img.shields.io/badge/Docker-deployments-blue)](#)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-workflows-black)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A question-wise archive of Tools in Data Science January 2026 work, with methods, code, deployments, outputs, and verification notes kept beside each assignment question.

This is not just a final-answer dump. The repo is designed as an audit trail: each folder should make it easy to see what was asked, what method was used, what artifact was produced, and how the result was checked.

## Contents

- [Best Examples](#best-examples)
- [Assignment Map](#assignment-map)
- [How to Reuse This Repo](#how-to-reuse-this-repo)
- [Repository Conventions](#repository-conventions)
- [README Coverage](#readme-coverage)
- [Contributing](#contributing)

## Best Examples

These are good starting points if you are browsing the repo or reusing its structure:

| Topic | Example | Why It Is Useful |
| --- | --- | --- |
| FastAPI CSV endpoint | [GA2 Q13](GA2/q13_fastapi_server/README.md) | Small deployable API with CSV loading, CORS, query filtering, Docker metadata, and local test commands. |
| Secure FastAPI upload | [GA2 Q18](GA2/q18_secure_upload/README.md) | File-validation service pattern with Docker and Python dependencies. |
| Playwright scraping in CI | [GA3 Q13](GA3/q13_github_action_scrape_table_sums_playwright/README.md) | Browser automation packaged with GitHub Actions for reproducible scraping. |
| Structured LLM API | [GA3 Q2](GA3/q02_llm_structured_output_fastapi_sentiment/README.md) | FastAPI wrapper for structured sentiment output and deployable API behavior. |
| Cross-lingual entity disambiguation | [GA4 Q16](GA4/q16_cross_lingual_entity_disambiguation/README.md) | Dataset-driven matching workflow using names, aliases, regions, dates, and scoring logic. |
| DuckDB analytics | [GA4 Q18](GA4/q18_duckdb_data_prep_retailco_analytics/README.md) | SQL transformation and analytics pattern for messy retail data. |
| Embeddings plus clustering | [GA5 Q1](GA5/q01_embeddings_kmeans/README.md) | Embedding generation, k-means clustering, and final answer extraction. |
| CLIP image search | [GA5 Q2](GA5/q02_clip_image_search/README.md) | Multimodal embedding search over image assets. |
| Geospatial Haversine analysis | [GA5 Q9](GA5/q09_geospatial_haversine/README.md) | Clear distance calculation pattern for location-based questions. |
| Evaluation and auditing | [GA6](GA6/README.md) | Property tests, rubrics, robustness checks, leakage detection, idempotency, and coverage gap patterns. |
| Visualization critique | [GA7](GA7/README.md) | Chart repair, narrative reconciliation, poisoned-document detection, and anomaly prioritization examples. |
| Cloud and MLOps APIs | [GA8](GA8/README.md) | Cloud Run, Cloud Functions, Docker builds, Ruff CI, Gemini API, and hash verification examples. |

## Assignment Map

| Folder | Questions Indexed | Main Methods Covered |
| --- | ---: | --- |
| [GA1](GA1/README.md) | 25 | Prompting, shell commands, debugging, Git-aware file work, spreadsheets, SQL, browser inspection, JSON conversion |
| [GA2](GA2/README.md) | 16 | Git history, GitHub Pages, Actions, dependency automation, Codespaces, Gists, FastAPI, Docker, Cloudflare |
| [GA3](GA3/README.md) | 18 | Structured LLM outputs, FastAPI endpoints, scheduled workflows, browser automation, PDF/video/audio extraction, web scraping |
| [GA4](GA4/README.md) | 20 | Excel, dbt, OpenRefine, JSON recovery, shell pipelines, FastAPI sentiment APIs, DuckDB, image/audio reconstruction, entity disambiguation |
| [GA5](GA5/README.md) | 21 | Embeddings, CLIP, topic modeling, Excel analytics, forecasting, geospatial computation, DuckDB, moving averages, RAG |
| [GA6](GA6/README.md) | 15 | Property-based testing, eval rubrics, robustness audits, data contracts, thresholds, flaky tests, leakage checks, coverage gaps |
| [GA7](GA7/README.md) | 15 | Chart critique, encoding fixes, data-narrative reconciliation, prompt repair, anomaly prioritization, poisoned-document detection |
| [GA8](GA8/README.md) | 15 | Secret hashing, Gemini APIs, FastAPI model services, Hugging Face Spaces, Docker, Ruff CI, Cloud Run, Cloud Functions |

## How to Reuse This Repo

1. Fork the repository.
2. Keep the `GA*/q##_topic/` structure so each question has its own home.
3. For each question, keep the writeup, data, code, generated outputs, Dockerfile, and deployment notes together.
4. Use the question README as a quick summary and the `.md` writeup as the detailed method.
5. Replace personal IDs, emails, tokens, deployed URLs, and generated answers with your own.
6. Do not submit copied answers. Use the structure to document your own method and verification.

## Repository Conventions

- Markdown writeups explain the problem, constraints, method, implementation, verification, and final answer where applicable.
- Code, data, Dockerfiles, deployment configs, Playwright scripts, generated images, and outputs stay next to the question that uses them.
- README files are navigation and audit summaries, not replacements for detailed question writeups.
- Preserved source material such as `original_README.md` stays intact.
- Secrets and local environment files are excluded through `.gitignore`.

## README Coverage

- Every GA folder from `GA1` to `GA8` has a README index.
- Question folders have README files that summarize the specific method and point to the detailed writeup.
- The root README links to the strongest examples and gives the overall map.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for cleanup, documentation, and contribution guidelines. The short version: keep changes question-scoped, document how you verified them, and never commit secrets.

## License

This repository is available under the [MIT License](LICENSE). Course prompts, third-party datasets, and platform-specific materials may have their own terms; use those responsibly.
