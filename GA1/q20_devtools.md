# GA1 — Q20: Use DevTools to Extract Hidden Input

## Problem Summary

The webpage contained a hidden input field with a secret value.  
The task required using browser DevTools to inspect the page and extract the value.

## Objective

Locate the hidden input element and retrieve its value.

## Steps Performed

1. Opened the webpage in the browser.
2. Opened DevTools using:
   - Right click → Inspect  
   - OR Cmd + Option + I (Mac)
3. Switched to the **Elements** tab.
4. Searched for `<input type="hidden">`.
5. Located the hidden input field.
6. Identified the `value` attribute.

## Extracted Hidden Input

```html
<input type="hidden" value="2ae08bf050">

