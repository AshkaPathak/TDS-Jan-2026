# GA4 — Q9: GitHub Copilot Code Generation

## Problem Summary

This task demonstrates how GitHub Copilot can generate working code from a natural language description.

We are asked to create a JavaScript function that splits an array into chunks of a fixed size (size = 3).

The function must accept an input array and return a new array where the elements are grouped into subarrays of length 3.

Example input:

[1,2,3,4,5,6,7,8]

Expected output:

[[1,2,3],[4,5,6],[7,8]]

---

## Function Implementation

The function iterates through the array in steps of 3 and slices the array into chunks.

```javascript
function transform(data) {
  const size = 3;
  const result = [];

  for (let i = 0; i < data.length; i += size) {
    result.push(data.slice(i, i + size));
  }

  return result;
}
```

---

## Explanation

1. The variable `size` defines the chunk size (3).
2. The loop iterates over the array in increments of 3.
3. `slice(i, i + size)` extracts a subarray of length up to 3.
4. Each chunk is pushed into the `result` array.
5. The final nested array structure is returned.

---

## Example Execution

Input:

[1,2,3,4,5,6,7,8]

Output:

[[1,2,3],[4,5,6],[7,8]]

---

## Conclusion

The Copilot-generated function correctly splits an array into chunks of size 3 and returns the expected nested array structure.
