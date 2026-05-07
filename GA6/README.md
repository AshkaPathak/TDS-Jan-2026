# GA6: LLM Evaluation and Quality Engineering

This folder contains GA6 question-wise work for the Tools in Data Science January 2026 course. The focus here is property-based testing, eval rubrics, robustness audits, data contracts, thresholding, flaky test analysis, leakage checks, idempotency checks, and coverage gaps. Each entry below names the question, the main artifact, and the method used so the folder works as a quick audit index.

## Question Index

| Question | Main Artifact | Method Used | Supporting Material |
| --- | --- | --- | --- |
| Q1: The Bug Hunter (Property-Based Testing) | [q01_bug_hunter_property_based_testing/q01_bug_hunter_property_based_testing.md](q01_bug_hunter_property_based_testing/q01_bug_hunter_property_based_testing.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q2: Build a Binary Eval Rubric | [q02_build_binary_eval_rubric/q02_build_binary_eval_rubric.md](q02_build_binary_eval_rubric/q02_build_binary_eval_rubric.md) | Applied an evaluation, audit, or testing method to detect failure modes and prioritize fixes. | question writeup and supporting files |
| Q3: Multi-Model Robustness Audit | [q03_multi_model_robustness_audit/q03_multi_model_robustness_audit.md](q03_multi_model_robustness_audit/q03_multi_model_robustness_audit.md) | Applied an evaluation, audit, or testing method to detect failure modes and prioritize fixes. | question writeup and supporting files |
| Q4: The Token Miser | [q04_token_miser/q04_token_miser.md](q04_token_miser/q04_token_miser.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q5: Data Contract Violation Detector | [q05_data_contract_violation_detector/q05_data_contract_violation_detector.md](q05_data_contract_violation_detector/q05_data_contract_violation_detector.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q6: The Slice Detective | [q06_slice_detective/q06_slice_detective.md](q06_slice_detective/q06_slice_detective.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q7: The Threshold Engineer | [q07_threshold_engineer/q07_threshold_engineer.md](q07_threshold_engineer/q07_threshold_engineer.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q8: The Flaky Test Finder | [q08_flaky_test_finder/q08_flaky_test_finder.md](q08_flaky_test_finder/q08_flaky_test_finder.md) | Applied an evaluation, audit, or testing method to detect failure modes and prioritize fixes. | question writeup and supporting files |
| Q9: The Embedding Auditor | [q09_embedding_auditor/q09_embedding_auditor.md](q09_embedding_auditor/q09_embedding_auditor.md) | Used embedding vectors or semantic similarity, then ranked or clustered results according to the task. | question writeup and supporting files |
| Q10: The Leakage Auditor | [q10_leakage_auditor/q10_leakage_auditor.md](q10_leakage_auditor/q10_leakage_auditor.md) | Applied an evaluation, audit, or testing method to detect failure modes and prioritize fixes. | question writeup and supporting files |
| Q11: Train-Test Contamination Scanner | [q11_train_test_contamination_scanner/q11_train_test_contamination_scanner.md](q11_train_test_contamination_scanner/q11_train_test_contamination_scanner.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q12: The Idempotency Prober | [q12_idempotency_prober/q12_idempotency_prober.md](q12_idempotency_prober/q12_idempotency_prober.md) | Applied an evaluation, audit, or testing method to detect failure modes and prioritize fixes. | data artifacts |
| Q13: Latency SLA Checker | [q13_latency_sla_checker/q13_latency_sla_checker.md](q13_latency_sla_checker/q13_latency_sla_checker.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q14: Benchmark Overfitter | [q14_benchmark_overfitter/q14_benchmark_overfitter.md](q14_benchmark_overfitter/q14_benchmark_overfitter.md) | Documented the problem, selected the appropriate tool or technique, implemented the answer, and recorded the verification step. | question writeup and supporting files |
| Q15: Coverage Gap Finder | [q15_coverage_gap_finder/q15_coverage_gap_finder.md](q15_coverage_gap_finder/q15_coverage_gap_finder.md) | Applied an evaluation, audit, or testing method to detect failure modes and prioritize fixes. | question writeup and supporting files |

## How to Read This Folder

Open the question artifact first. If the question has code, data, generated media, a Dockerfile, or deployment configuration, those files live in the same question folder. README files inside question folders summarize the runnable method and point to the detailed writeup.

## Verification Pattern

Solutions are verified with the artifact that best matches the task: command output, API response, deployed URL, SQL result, spreadsheet calculation, generated file, model/API response, or manual inspection note.
