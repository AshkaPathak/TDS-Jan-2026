# GA2 — Q11: Configure a Codespace Devcontainer (0.5 marks)

## Problem Summary

Set up a GitHub Codespaces devcontainer that mirrors the expected tooling stack.

The grader requires:

- A `.devcontainer/devcontainer.json` file
- `name` must be exactly: `ga2-7846df`
- Must use the feature: `ghcr.io/devcontainers/features/python:1`
- Must install VS Code extensions:
  - `astral-sh.uv`
  - `ms-python.python`
- Must run a `postCreateCommand` that installs FastAPI using uv:
  - `uv pip install fastapi`

Then, after launching a Codespace, print:

```bash
echo $GITHUB_REPOSITORY $GITHUB_TOKEN

