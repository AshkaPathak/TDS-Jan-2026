# GA1: Tools in Data Science Foundations

This folder contains GA1 question-wise work for the Tools in Data Science January 2026 course. The focus here is prompting, command-line work, code debugging, Git-aware file operations, spreadsheets, SQL, browser inspection, and compact data representation. Each entry below names the question, the main artifact, and the method used so the folder works as a quick audit index.

## Question Index

| Question | Main Artifact | Method Used | Supporting Material |
| --- | --- | --- | --- |
| Q1: Debug and Improve a Failing Prompt | [q01_promptops.md](q01_promptops.md) | Used an LLM or prompt/API workflow with structured inputs, controlled outputs, and validation against the expected format. | question writeup and supporting files |
| Q2: Get an LLM to say "Yes" | [q02_llm_yes.md](q02_llm_yes.md) | Used an LLM or prompt/API workflow with structured inputs, controlled outputs, and validation against the expected format. | question writeup and supporting files |
| Q3: Bash Pipeline using `llm` CLI | [q03_bashpipeline.md](q03_bashpipeline.md) | Used an LLM or prompt/API workflow with structured inputs, controlled outputs, and validation against the expected format. | question writeup and supporting files |
| Q4: Vibe Code a data crunching app | [q04_vibecode.md](q04_vibecode.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q5: Deploy a quiz app using Vercel v0 | [q05_vercel_v0_quiz.md](q05_vercel_v0_quiz.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q6: Debug a Python Project | [q06_debug_python.md](q06_debug_python.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q7: q07_debug_url_validation | [q07_debug_url_validation.md](q07_debug_url_validation.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q8: AI Tool Selection and Architecture Design | [q08_ai_tool_architecture.md](q08_ai_tool_architecture.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q9: Refactor Python Code to PEP 8 (Rename Symbol) | [q09_refactor_pep8.md](q09_refactor_pep8.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q10: Replace Across Files (Shell Commands) | [q10_replace_across_files.md](q10_replace_across_files.md) | Used shell commands and pipelines to parse, transform, aggregate, and verify the requested output. | question writeup and supporting files |
| Q11: Reorganize Files by Category and Verify SHA256 | [q11_reorganize_by_category_hash.md](q11_reorganize_by_category_hash.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q12: Record Terminal Session Using Asciinema | [q12_asciinema.md](q12_asciinema.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q13: GitHub Copilot CLI (Asciinema Recording) | [q13_copilot_cli.md](q13_copilot_cli.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q14: Excel Formula Evaluation (Office 365) | [q14_excel_formula.md](q14_excel_formula.md) | Traced spreadsheet formulas or analytics steps carefully and verified the numerical result. | question writeup and supporting files |
| Q15: Google Sheets Formula Evaluation | [q15_google_sheets.md](q15_google_sheets.md) | Traced spreadsheet formulas or analytics steps carefully and verified the numerical result. | question writeup and supporting files |
| Q16: Infer SQL Schema from CSVs (E-commerce) | [q16_sql_schema.md](q16_sql_schema.md) | Solved with SQL-style transformations, aggregation, joins, filtering, and a final query/result check. | question writeup and supporting files |
| Q17: Average Salary per Department (GROUP BY) | [q17_groupby_avg.md](q17_groupby_avg.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q18: q18 semantic search | [q18_semantic_search/README.md](q18_semantic_search/README.md) | Used embedding vectors or semantic similarity, then ranked or clustered results according to the task. | Python API/service code, Python dependencies, data artifacts |
| Q19: q19 similarity api | [q19_similarity_api/README.md](q19_similarity_api/README.md) | Implemented the solution in Python with a small service or script and documented how to run it. | Python API/service code, Python dependencies |
| Q20: Use DevTools to Extract Hidden Input | [q20_devtools.md](q20_devtools.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q21: CSS Featured-Sale Discount Sum | [q21_css_featured_sale_discount_sum.md](q21_css_featured_sale_discount_sum.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q22: Hidden HTML Trick Question | [q22_hidden_html_trick_question.md](q22_hidden_html_trick_question.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q25: AI Cost Optimization for StreamAnalytics | [q25_ai_cost_optimization_streamanalytics.md](q25_ai_cost_optimization_streamanalytics.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q26: q26 cache | [q26_cache/README.md](q26_cache/README.md) | Implemented the solution in Python with a small service or script and documented how to run it. | Python API/service code, Python dependencies |
| Q26: q26 columnar json | [q26_columnar_json/README.md](q26_columnar_json/README.md) | Parsed, repaired, flattened, or transformed JSON into the schema required by the grader. | data artifacts |

## How to Read This Folder

Open the question artifact first. If the question has code, data, generated media, a Dockerfile, or deployment configuration, those files live in the same question folder. README files inside question folders summarize the runnable method and point to the detailed writeup.

## Verification Pattern

Solutions are verified with the artifact that best matches the task: command output, API response, deployed URL, SQL result, spreadsheet calculation, generated file, model/API response, or manual inspection note.
