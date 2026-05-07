# GA8: MLOps, Cloud APIs, Docker, and GCP Deployment

This folder contains GA8 question-wise work for the Tools in Data Science January 2026 course. The focus here is secret hashing, Gemini API calls, FastAPI model services, Hugging Face Spaces, Docker multi-stage builds, Ruff CI, Cloud Run, Cloud Functions, and hash verification APIs. Each entry below names the question, the main artifact, and the method used so the folder works as a quick audit index.

## Question Index

| Question | Main Artifact | Method Used | Supporting Material |
| --- | --- | --- | --- |
| Q1: GitHub Actions Secret Hash Chain | [q01_secret_hash_chain/q01_secret_hash_chain.md](q01_secret_hash_chain/q01_secret_hash_chain.md) | Used a GitHub Actions workflow, trigger configuration, and run-log verification. | question writeup and supporting files |
| Q2: GCP Gemini API Math Puzzle | [q02_gemini_math_puzzle/q02_gemini_math_puzzle.md](q02_gemini_math_puzzle/q02_gemini_math_puzzle.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | question writeup and supporting files |
| Q3: Deploy a FastAPI Iris Classifier | [q03_deploy_fastapi_iris_classifier/q03_deploy_fastapi_iris_classifier.md](q03_deploy_fastapi_iris_classifier/q03_deploy_fastapi_iris_classifier.md) | Implemented a FastAPI endpoint with explicit request/response behavior, local testing, and deployment-ready dependencies. | Python API/service code, Docker deployment, Python dependencies |
| Q4: Hugging Face Spaces Sentiment Analysis API | [q04_hf_sentiment_api/q04_hf_sentiment_api.md](q04_hf_sentiment_api/q04_hf_sentiment_api.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | Python API/service code, Docker deployment, Python dependencies |
| Q5: Docker Multi-stage Build — Train and Verify an ML Model | [q05_docker_multistage/q05_docker_multistage.md](q05_docker_multistage/q05_docker_multistage.md) | Packaged the solution with Docker and documented build/run behavior for reproducibility. | Docker deployment |
| Q6: MLOps Bash Script — Deterministic Output | [q06_bash_script/q06_bash_script.md](q06_bash_script/q06_bash_script.md) | Used shell commands and pipelines to parse, transform, aggregate, and verify the requested output. | question writeup and supporting files |
| Q7: Pre-commit Hooks + CI Gate with Ruff | [q07_ruff_ci/q07_ruff_ci.md](q07_ruff_ci/q07_ruff_ci.md) | Implemented the solution in Python with a small service or script and documented how to run it. | Python API/service code |
| Q8: MLOps Concepts — Hash Verified Quiz | [q08_mlops_quiz/q08_mlops_quiz.md](q08_mlops_quiz/q08_mlops_quiz.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q9: GCP Cloud Run — Deploy a Compute Service | [q09_compute_service/q09_compute_service.md](q09_compute_service/q09_compute_service.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | Python API/service code, Docker deployment, Python dependencies |
| Q10: GCP Cloud Functions — HTTP Triggered Text Processor | [q10_text_processor/q10_text_processor.md](q10_text_processor/q10_text_processor.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | Python API/service code, Docker deployment, Python dependencies |
| Q11: GCP AI Studio — Gemini Text Classification | [q11_gemini_text_classification/q11_gemini_text_classification.md](q11_gemini_text_classification/q11_gemini_text_classification.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | question writeup and supporting files |
| Q12: GCP Cloud Run — Deploy an ML Classifier | [q12_ml_classifier/q12_ml_classifier.md](q12_ml_classifier/q12_ml_classifier.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | Python API/service code, Docker deployment, Python dependencies |
| Q13: GCP Cloud Run — Environment Variable Configuration | [q13_env_config_service/q13_env_config_service.md](q13_env_config_service/q13_env_config_service.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | Python API/service code, Docker deployment, Python dependencies |
| Q14: GCP Cloud Run — Hash Verification API | [q14_hash_verification_api/q14_hash_verification_api.md](q14_hash_verification_api/q14_hash_verification_api.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | Python API/service code, Docker deployment, Python dependencies |
| Q15: GCP AI Studio — Gemini JSON Data Extraction | [q15_gemini_json_extraction/q15_gemini_json_extraction.md](q15_gemini_json_extraction/q15_gemini_json_extraction.md) | Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification. | question writeup and supporting files |

## How to Read This Folder

Open the question artifact first. If the question has code, data, generated media, a Dockerfile, or deployment configuration, those files live in the same question folder. README files inside question folders summarize the runnable method and point to the detailed writeup.

## Verification Pattern

Solutions are verified with the artifact that best matches the task: command output, API response, deployed URL, SQL result, spreadsheet calculation, generated file, model/API response, or manual inspection note.
