# GA6 — Q10: The Leakage Auditor

## Problem Summary

You are given a benchmark of 60 science questions along with a reference corpus representing text likely seen during model training.

Each question has:
- question text
- is_correct (1 if model answered correctly, 0 otherwise)

Your task is to detect **data contamination** using n-gram overlap and compute:

1. contaminated_count
2. reported_accuracy
3. adjusted_accuracy

---

## Key Idea

If a question shares too many exact phrases (8-grams) with the corpus, it is likely memorized rather than understood.

---

## Tokenization Rule

Apply the same preprocessing to both corpus and questions:

- convert to lowercase  
- replace all non-alphanumeric characters with spaces  
- split on whitespace  
- remove empty tokens  

---

## 8-gram Overlap Score

For each question:

overlap_score =  
(number of 8-grams in the question that appear in corpus)  
/  
(total number of 8-grams in the question)

If a question has fewer than 8 tokens, overlap_score = 0.

---

## Contamination Rule

A question is considered contaminated if:

overlap_score > 0.3

---

## Implementation Steps

1. Tokenize the entire corpus
2. Generate all 8-grams from corpus and store in a set
3. For each question:
   - tokenize
   - generate 8-grams
   - compute overlap score
   - mark as contaminated if overlap > 0.3
4. Count total contaminated questions

---

## Accuracy Computation

### Reported Accuracy

reported_accuracy =  
(total correct answers / total questions) × 100

---

### Adjusted Accuracy

Only consider **non-contaminated questions**:

adjusted_accuracy =  
(correct answers on clean questions / number of clean questions) × 100

---

## Final Answer

10,70.00,66.00

Where:
- contaminated_count = 10  
- reported_accuracy = 70.00  
- adjusted_accuracy = 66.00  

---

## Why This Works

- 8-gram overlap detects verbatim memorization from training data  
- Threshold > 0.3 filters strongly overlapping questions  
- Reported accuracy includes contaminated samples and is inflated  
- Adjusted accuracy reflects true generalization performance  
- The drop from 70.00 to 66.00 quantifies leakage impact
