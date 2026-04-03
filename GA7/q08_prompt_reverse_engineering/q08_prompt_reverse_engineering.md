# GA7 — Q8: Prompt Reverse Engineering

## Problem Summary

The task is to reverse-engineer the hidden prompt specification from a given high-quality artifact. The inferred prompt must explicitly encode six structural elements: audience, output format, tone/style, key findings to emphasize, length constraint, and structure rules. After constructing the prompt (minimum 50 words), an LLM response must be generated using that prompt. The final submission must include only two sections: Prompt and LLM Response.

---

## Step 1 — Inferred Prompt Specification

From the artifact:

- **Audience:** Bank risk committee (decision-making audience)
- **Output Format:** Three-paragraph narrative memo
- **Tone/Style:** Product analytics weekly brief — concrete, data-driven, concise
- **Key Findings (limit 2–3):**
  - Site C worsened after intervention
  - Site A improved the most
  - Variance widened across sites
  - Activation improved while retention lagged (critical insight)
- **Length Constraint:** 320–420 words
- **Structure Rules:**
  - Open with a question
  - Identify turning point
  - Show baseline shift
  - Anchor claims with numbers
  - Include implication sentence
  - End with action: ship one test this sprint

---

## Final Submission

### Prompt:
Write a three-paragraph narrative memo for a bank risk committee in a product analytics weekly brief tone. The memo should be concrete, data-driven, and avoid generic statements. Open with a question that frames the core issue. Emphasize only 2–3 key findings: that site C worsened after intervention, site A improved the most, and that variance widened across sites indicating misalignment. Clearly identify the turning point, describe where the baseline shifted, and anchor each claim to at least one specific number. Include the critical insight that activation improved while retention lagged. Maintain a length between 320 and 420 words. Conclude with a clear action-oriented implication, specifically recommending shipping one test this sprint.

### LLM Response:
What actually changed after the intervention, and are we optimizing the right signal? For the risk committee, the headline is not uniform improvement but divergence: site C deteriorated post-intervention while site A delivered the strongest gains. The older narrative suggested steady growth, but the updated data shows dispersion increasing across sites. For example, while site A’s activation rose meaningfully, site C’s corresponding metric declined, creating a wider spread than previously observed. This indicates that performance is no longer moving in sync, and the assumption of consistent uplift across sites is no longer valid.

The turning point appears immediately after the intervention rollout, where the baseline behavior begins to shift. Prior to this, site performance tracked relatively closely, but post-change, the gap widened significantly. The key signal most readers miss is that activation improved, but retention lagged behind. This creates a misleading sense of progress if only top-line activation is considered. Anchoring to the numbers, activation increases are visible across at least one major site, but retention metrics do not follow the same trajectory, suggesting that early gains are not translating into sustained engagement.

The implication is clear: our default playbook is now misaligned with actual system behavior. Optimizing for activation alone is insufficient when retention does not keep pace. The increased variance across sites further reinforces that a single strategy is no longer universally effective. We need to isolate what is driving success in site A and failure in site C. The immediate next step is to ship one targeted test this sprint focused on aligning activation gains with retention outcomes.
