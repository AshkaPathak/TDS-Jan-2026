# GA1 — Q1: Debug and Improve a Failing Prompt

## Problem Summary
The original prompt attempted to classify content moderation safety level but failed due to ambiguity and lack of structure.

## Original Failing Prompt
What safety level is this content moderation? '[text]'. Just give me the level.

## Issues Identified
1. No defined safety-level scale.
2. No structured output format specified.
3. No handling of edge cases (empty/ambiguous input).
4. No context or policy definition for classification.

## Strategy to Fix
- Define explicit safety levels with descriptions.
- Force strict JSON output.
- Add edge case handling.
- Require a reason for interpretability.
- Ensure production-ready formatting.

## Improved Prompt
You are a content moderation system.

Task:
Classify the given text into one of the following safety levels:

Level 0: Safe – No harmful or abusive content.
Level 1: Mildly Unsafe – Contains mild profanity or insensitive language.
Level 2: Moderately Unsafe – Contains harassment, hate speech, or abusive content targeting individuals or groups.
Level 3: Severe – Contains threats, incitement to violence, or extreme harmful content.

Instructions:
- Return output strictly in JSON format.
- Do NOT include any explanation outside JSON.
- If input text is empty or unclear, classify as "Unknown".
- Always include both the level number and a short reason.

Output format:
{
  "level": <number or "Unknown">,
  "reason": "<short explanation>"
}

Text to classify:
"[TEXT]"

## Final JSON Submission
{
  "problems": [
    "The prompt does not define what safety levels exist or what they mean",
    "No output format is specified, leading to inconsistent responses",
    "The prompt does not handle edge cases like empty or ambiguous input",
    "There is no instruction to provide structured output suitable for automation"
  ],
  "improvedPrompt": "You are a content moderation system.\n\nTask:\nClassify the given text into one of the following safety levels:\n\nLevel 0: Safe – No harmful or abusive content.\nLevel 1: Mildly Unsafe – Contains mild profanity or insensitive language.\nLevel 2: Moderately Unsafe – Contains harassment, hate speech, or abusive content targeting individuals or groups.\nLevel 3: Severe – Contains threats, incitement to violence, or extreme harmful content.\n\nInstructions:\n- Return output strictly in JSON format.\n- Do NOT include any explanation outside JSON.\n- If input text is empty or unclear, classify as \"Unknown\".\n- Always include both the level number and a short reason.\n\nOutput format:\n{\n  \"level\": <number or \"Unknown\">,\n  \"reason\": \"<short explanation>\"\n}\n\nText to classify:\n\"[TEXT]\"",
  "improvements": [
    "Defined explicit safety levels to remove ambiguity",
    "Specified strict JSON output format for consistent structure",
    "Added edge case handling for empty or unclear input",
    "Included requirement for reason to improve interpretability"
  ]
}

## Result
PASS
