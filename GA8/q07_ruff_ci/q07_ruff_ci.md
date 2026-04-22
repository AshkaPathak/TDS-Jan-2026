# GA8 — Q7: Pre-commit Hooks + CI Gate with Ruff

## Problem Summary
Set up Ruff as both a local pre-commit hook and a CI gate using GitHub Actions to enforce Python code quality before commits and before merging pull requests. The final submission requires the Ruff version used and a successful GitHub Actions workflow run URL.

## What is Ruff?
Ruff is a fast Python linter and formatter written in Rust. It replaces flake8, isort, and black, combining linting and formatting into a single tool with significantly higher performance.

## What are Pre-commit Hooks?
Pre-commit hooks run automatically before a commit is created. If a hook fails, the commit is blocked until issues are fixed. This ensures only clean and properly formatted code is committed to the repository.

## Local vs CI Checks
Pre-commit hooks run locally before commits, catching issues early. CI checks run on GitHub during pull requests, ensuring all code merged into the main branch meets quality standards. Using both provides strong enforcement at two levels.

## Step 1 — Repository Setup
A public GitHub repository named ga8_q07 was created. A simple Python file main.py was added with basic content to initialize the repository.

## Step 2 — Pre-commit Configuration
A .pre-commit-config.yaml file was created with Ruff hooks and standard formatting checks including trailing whitespace removal, end-of-file fixing, YAML validation, and merge conflict detection. Ruff version v0.4.4 was explicitly used to match requirements. Pre-commit was installed locally and activated so hooks run automatically on commit.

## Step 3 — CI Workflow Setup
A GitHub Actions workflow file was created at .github/workflows/ruff-ci.yml. The workflow triggers on pull_request events, sets up Python 3.11, installs ruff==0.4.4, and runs both ruff check . and ruff format --check . to validate code quality and formatting.

## Step 4 — Creating Violations
A new branch feature/add-analysis was created. A file analysis.py was added containing unused imports, improper spacing, and formatting issues to intentionally trigger Ruff violations.

## Step 5 — Pre-commit Execution
When committing the file, pre-commit hooks ran automatically and detected issues. The command python -m pre_commit run --all-files was used to fix all violations. The corrected file was then committed successfully.

## Step 6 — Pull Request and CI Execution
A pull request was opened from feature/add-analysis to main. This triggered the GitHub Actions workflow automatically.

## Step 7 — Successful CI Run
After fixing all issues, the workflow completed successfully with a green check. The run verified that Ruff linting and formatting checks passed.

## Final Answer
ruff 0.4.4|https://github.com/AshkaPathak/ga8_q07/actions/runs/24772206717

## Conclusion
This setup enforces code quality at two levels: locally using pre-commit hooks and globally using CI checks. Ruff provides a fast and unified solution for linting and formatting, ensuring clean, consistent, and maintainable code across the project.
