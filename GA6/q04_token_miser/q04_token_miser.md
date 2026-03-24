# GA6 — Q4: The Token Miser

## Problem Summary

The task was to write a prompt of **at most 4 words** that classifies a customer request into one of these urgency levels:

- High
- Medium
- Low

The evaluator tests the prompt on **10 randomized cases** using **gpt-4.1-mini**, and the prompt passes only if it gets at least **8/10 correct**.

The model must return **only the category name**.

---

## Core Challenge

This was not a normal classification problem where I directly answer the requests.

Instead, I had to write a **tiny meta-prompt** that another model would use to perform the classification.

That created two simultaneous constraints:

1. The prompt had to be extremely short: **4 words or fewer**
2. The prompt still had to:
   - make the model understand it was doing classification
   - restrict the output to the allowed labels
   - avoid extra text such as explanations, prefixes, or conversational responses

---

## Initial Observations

From the sample cases, the expected behavior was:

- Clearly critical failures such as:
  - payment gateway returning 500 errors
  - production database corruption
  - login broken after an update  
  should be classified as **High**

- Routine, cosmetic, or future/planned requests such as:
  - upgrading a subscription next month
  - logo slightly off-center
  - adding dark mode
  - changing a password  
  should be classified as **Low**

This meant the model needed to separate **real operational urgency** from normal support or product requests.

---

## Failed Prompt Attempts and What They Revealed

I tested several short prompts and used the evaluator feedback to understand the failure mode.

### Attempt 1

`Classify urgency: High/Medium/Low`

This failed because the model often returned outputs like:

- `Urgency: High`
- conversational text
- other extra tokens

So even though the intent was clear, the output format was not strict enough.

---

### Attempt 2

`Return urgency High/Medium/Low only`

This improved formatting slightly, but the model still sometimes echoed the wording and sometimes over-classified routine requests as urgent.

---

### Attempt 3

`Urgency label only`

This caused outputs such as:

- `Low urgency`
- `Urgency: High`

So using the word **urgency** itself increased the chance that the model would repeat it in the answer.

---

### Attempt 4

`Reply High/Medium/Low`

This looked promising because it compressed the label space, but in practice it still allowed conversational completions in some cases.

---

### Attempt 5

`Classify High/Medium/Low only`

This was the first strong candidate.

It achieved **7/10**, which was the closest near-pass.

However, it still failed on some clearly low-priority examples such as:

- subscription upgrade next month
- logo slightly off-center
- feature request like dark mode

In those cases, the model tended to output **Medium** instead of **Low**.

This showed that the overall structure was good, but the model still had a slight bias toward assigning **Medium** to borderline non-urgent requests.

---

## Key Insight

Since `Classify High/Medium/Low only` already reached **7/10**, the right move was not to completely change the wording.

Instead, I kept the same successful structure and changed the **order of labels**.

The reason was simple:

- the model already understood the task
- the format was mostly correct
- the remaining problem was bias on uncertain cases

So I reordered the labels to bias the model slightly toward **Low** for borderline requests.

---

## Final Passing Prompt

`Classify Low/Medium/High only`

This prompt passed the evaluator.

---

## Why This Worked

This final prompt worked because it combined all the important properties:

### 1. `Classify`
This clearly tells the model that the task is classification, not explanation or conversation.

### 2. `Low/Medium/High`
This restricts the output space to the exact allowed labels.

Using slash-separated labels compresses multiple answer choices into one token group, which is ideal under a 4-word constraint.

### 3. `only`
This strongly nudges the model to output just the label and nothing else.

### 4. Label order matters
In earlier attempts, borderline low-priority cases were being classified as **Medium**.

By placing `Low` first, the model became more likely to assign **Low** to cosmetic, routine, and feature-request style inputs, which matched the expected grading behavior better.

---

## Final Answer Submitted

`Classify Low/Medium/High only`

---

## Outcome

The prompt successfully met all constraints:

- at most 4 words
- valid urgency labels
- concise output
- strong enough generalization to pass the randomized evaluator

---

## Conclusion

The main difficulty in this question was not understanding urgency itself, but compressing the instruction enough that the model still behaved correctly.

The successful strategy was:

1. make the prompt explicitly classification-oriented
2. constrain the label space with slash-separated options
3. force concise output with `only`
4. tune label ordering to correct borderline decision bias

The final passing prompt was:

`Classify Low/Medium/High only`
