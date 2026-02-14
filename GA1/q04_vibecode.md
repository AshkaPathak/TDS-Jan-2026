# GA1 — Q4: Vibe Code a data crunching app

## Problem Summary

The task required writing a prompt that instructs GPT-5 Nano to generate the body of an async JavaScript function that fetches JSON from `url` and returns the sum of `data[].number`.

## Initial Issue

Early attempts either:
- Provided direct implementation instead of a prompt
- Generated a full function declaration (causing grader errors)
- Failed to reference the correct JSON structure (`json.data`)

## Strategy

- Clearly instruct the model to output only the function body
- Forbid function declarations or wrapping code
- Specify expected JSON shape (`{ data: [...] }`)
- Require returning the computed sum

## Final Prompt Submitted

Output only the JavaScript function body. Do not include a function declaration or any wrapping code. Assume `url` already exists. Fetch JSON from `url`, access `json.data`, and return the sum of all `data[].number` values.


## Improvements

- Prevented nested function syntax errors
- Ensured correct JSON field access
- Removed spoonfeeding while keeping structural clarity
- Produced grader-compatible output

## Result

PASS
