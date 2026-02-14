# GA1 – Question 3 (Bash pipeline using `llm`)

## Task
Write a bash pipeline command using Simon Willison’s `llm` CLI tool to:
- list all JavaScript files in the current directory
- summarize the purpose of each file in **one line each**

## Final command
```bash
ls *.js | xargs -I{} sh -c 'echo "File: {}"; llm "Summarize the purpose of this JavaScript file in one line." < "{}"'
