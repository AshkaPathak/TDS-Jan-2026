# GA1 — Q9: Refactor Python Code to PEP 8 (Rename Symbol)

## Problem Summary

The provided Python module worked correctly but violated PEP 8 naming conventions by using camelCase for functions and variables. The task was to refactor **only the non-compliant names** to `snake_case` using **VS Code Rename Symbol (F2)** to safely update all references.

### Constraints (Must Not Change)
- Class names (PascalCase) — `DataProcessor`
- Constants (UPPER_CASE) — `MAX_ITEMS`

---

## Names to Refactor

The prompt required renaming **all occurrences** of these identifiers:

- `getUserData` → `get_user_data`
- `processItems` → `process_items`
- `maxRetries` → `max_retries`
- `currentIndex` → `current_index`

Important: `currentIndexItem` was preserved exactly as expected by the checker, while the underlying attribute reference was refactored to `current_index`.

---

## Approach / Methodology

1. Opened `refactor_me.py` in VS Code.
2. Used **Rename Symbol (F2)** on each target identifier to ensure:
   - every reference updates safely
   - no accidental renames via find/replace
3. Verified the following:
   - No remaining occurrences of `getUserData`, `processItems`, `maxRetries`, or `self.currentIndex`
   - Class name and constants unchanged
   - Code behavior unchanged

---

## Final Refactored Code (Submitted)

```python
"""
Machine Learning Model Refactoring

This module handles machine learning pipeline.
Note: This code uses camelCase naming which violates PEP 8.
Refactor the non-compliant names to snake_case.

DO NOT change:
- Class names (PascalCase is correct for classes)
- Constants (UPPER_CASE is correct for constants)
"""

import json
from typing import List, Dict, Optional


class DataProcessor:
    """Main data processor class - DO NOT RENAME"""

    MAX_ITEMS = 1000  # Constant - DO NOT RENAME

    def __init__(self, config: Dict):
        self.config = config
        self.current_index = 0  # Track current position
        self.items = []

    def get_user_data(self, user_id: str) -> Optional[Dict]:
        """Fetch user data from the API"""
        # Using get_user_data to retrieve information
        if not user_id:
            return None

        # Call get_user_data multiple times for retry logic
        data = self._fetch_data(user_id)
        if data:
            # get_user_data succeeded
            result = self.process_items(data)
            return result
        return None

    def process_items(self, items: List[Dict]) -> List[Dict]:
        """Process items and apply transformations"""
        processed = []
        self.current_index = 0  # Reset current_index

        for item in items:
            # process_items handles each item
            if self.max_retries(item):
                formatted = self.currentIndexItem(item)
                processed.append(formatted)
                self.current_index += 1  # Increment current_index

        # process_items returns processed items
        return processed

    def max_retries(self, data: Dict) -> bool:
        """Validate input data structure"""
        # max_retries checks required fields
        if not isinstance(data, dict):
            return False

        required_fields = ['id', 'name', 'value']
        # max_retries ensures all fields present
        for field in required_fields:
            if field not in data:
                return False

        # max_retries passed all checks
        return True

    def currentIndexItem(self, item: Dict) -> Dict:
        """Format a single item - uses current_index prefix"""
        # Note: Method name intentionally uses current_index
        # This tests that you DON'T rename the variable inside the method name
        return {
            'id': item['id'],
            'processed': True,
            'index': self.current_index  # Reference to variable
        }

    def _fetch_data(self, user_id: str) -> Optional[List[Dict]]:
        """Internal helper method"""
        # Simulate API call
        return [{'id': user_id, 'name': 'Test', 'value': 84}]


def main():
    """Main execution function"""
    processor = DataProcessor(config={})

    # Test get_user_data
    user_data = processor.get_user_data("user123")
    if user_data:
        # Process using process_items
        items = [user_data]
        results = processor.process_items(items)

        # Validate using max_retries
        for result in results:
            if processor.max_retries(result):
                print(f"Processed item at index {processor.current_index}")


if __name__ == "__main__":
    main()
```

---

## Result
PASS
