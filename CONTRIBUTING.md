# Contributing

Thanks for improving this TDS January 2026 archive. The goal is to keep the repo useful as a readable, reproducible record of question-solving methods.

## What Good Contributions Look Like

- Keep each change scoped to one assignment or question folder.
- Add or update a README when the method, runtime, deployment, or verification changes.
- Keep runnable code beside the question it belongs to.
- Include exact commands when a result depends on command-line execution.
- Mention how the answer was verified: API response, hash, SQL result, generated file, deployed URL, screenshot, or manual inspection.

## Documentation Style

Use this structure for question READMEs when possible:

1. Problem or task summary
2. Method used
3. Files in the folder
4. Run or reproduce commands
5. Verification notes

Keep wording direct. A future reader should be able to decide quickly whether a folder is relevant and how to rerun the solution.

## Safety Rules

- Do not commit `.env` files, API keys, tokens, private credentials, or generated secrets.
- Replace personal identifiers before reusing this structure in another repository.
- Do not add large generated files unless the question specifically requires them.
- Do not rewrite preserved source prompts such as `original_README.md` unless the goal is explicitly to correct that source record.

## Pull Request Checklist

- The change is limited to the relevant assignment/question files.
- README links still point to existing files.
- Commands in the README have been checked or are clearly marked as examples.
- `git status` contains no accidental generated files.
- No secrets or personal credentials are included.
