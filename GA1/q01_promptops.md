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