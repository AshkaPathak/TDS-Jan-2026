# GA1 — Q3: Bash Pipeline using `llm` CLI

## Problem Summary

The task required writing a bash pipeline using Simon Willison’s `llm` CLI tool to summarize all JavaScript files in the current directory in one line each.

## Initial Considerations

The solution must:

- List all `.js` files in the current directory  
- Process each file individually  
- Pass file content into the `llm` CLI  
- Produce exactly one summary per file  
- Be executable as a valid Unix pipeline  

## Potential Issues

- Simply listing files does not process file content.  
- The `llm` CLI requires input via standard input (stdin).  
- Handling multiple files requires iteration (`xargs` or a loop).  
- If no `.js` files exist, `ls *.js` may raise an error.  

## Strategy

- Use `ls *.js` to list JavaScript files.  
- Use `xargs` to iterate through each file.  
- Use `sh -c` to allow multiple commands per file.  
- Use input redirection (`< filename`) to pass file content to `llm`.  
- Print the filename before each summary for clarity.  

## Final Command

```bash
ls *.js | xargs -I{} sh -c 'echo "File: {}"; llm "Summarize the purpose of this JavaScript file in one line." < "{}"'

## Result
PASS