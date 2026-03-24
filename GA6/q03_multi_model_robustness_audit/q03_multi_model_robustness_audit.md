# GA6 — Q3: Multi-Model Robustness Audit

## Problem Summary

The task was to find the **shortest prompt** formed by selecting a subset of instruction fragments such that, after combining:

- the **base logits** for each model,
- the **selected fragment logits**, and
- any applicable **pair bonuses**,

the resulting prompt achieved:

- **Macro-Mean accuracy ≥ 97**
- **Model Floor accuracy ≥ 92**

for all four models.

The answer format required by the portal was:

`IDs; WC; Mean; Floor`

where:

- `IDs` = selected instruction IDs
- `WC` = total word count
- `Mean` = macro-average accuracy across the 4 models
- `Floor` = minimum model accuracy among the 4 models

---

## Important Insight

At first glance, the table values look like direct accuracy adjustments, but that interpretation is incorrect.

The correct scoring method is:

1. Start from the **base logits** for each model.
2. Add the logits contributed by each selected instruction.
3. Add any listed **pair bonuses** between selected instruction pairs.
4. Convert each final model logit into an accuracy percentage using the **sigmoid function**:

\[
\text{accuracy} = \frac{100}{1 + e^{-x}}
\]

where \(x\) is the final logit for that model.

This was the key reason earlier low-word-count guesses failed even though they looked mathematically plausible under simple linear addition.

---

## Extracted Base Logits

The question provided the following base logits:

- **gpt-4o** = -1.67
- **gpt-4.1** = -1.76
- **gpt-4.1-mini** = -2.28
- **gpt-5-mini** = -0.15

---

## Correct Selected Instructions

The shortest valid subset was:

- **I7**
- **I10**
- **I12**
- **I15**
- **I19**

So the selected prompt ID list is:

`I7,I10,I12,I15,I19`

---

## Total Word Count

The portal-accepted total word count for this subset was:

`40`

---

## Final Logits After Adding Selected Instructions and Pair Bonuses

Using the correct logit-space combination method, the final logits became:

- **gpt-4o** = 2.79
- **gpt-4.1** = 4.10
- **gpt-4.1-mini** = 4.28
- **gpt-5-mini** = 4.95

---

## Convert Logits to Accuracy

Using:

\[
\text{accuracy} = \frac{100}{1 + e^{-x}}
\]

we get:

### 1. gpt-4o
\[
\frac{100}{1 + e^{-2.79}} \approx 94.21
\]

### 2. gpt-4.1
\[
\frac{100}{1 + e^{-4.10}} \approx 98.37
\]

### 3. gpt-4.1-mini
\[
\frac{100}{1 + e^{-4.28}} \approx 98.63
\]

### 4. gpt-5-mini
\[
\frac{100}{1 + e^{-4.95}} \approx 99.30
\]

So the four final accuracies were:

- **94.21**
- **98.37**
- **98.63**
- **99.30**

---

## Macro-Mean

\[
\text{Macro-Mean} = \frac{94.21 + 98.37 + 98.63 + 99.30}{4}
\]

\[
= \frac{390.51}{4} = 97.6275
\]

Rounded to 2 decimals:

`97.63`

---

## Model Floor

The minimum among the 4 model accuracies is:

`94.21`

So:

- **Macro-Mean** = `97.63`
- **Model Floor** = `94.21`

Both satisfy the required thresholds:

- Macro-Mean ≥ 97 ✅
- Model Floor ≥ 92 ✅

---

## Final Answer Submitted

```text
I7,I10,I12,I15,I19;40;97.63;94.21
