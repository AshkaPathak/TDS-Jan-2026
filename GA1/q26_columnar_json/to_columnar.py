import json
from pathlib import Path

INPUT = Path("data.json")
OUTPUT = Path("data_columnar.json")

data = json.loads(INPUT.read_text(encoding="utf-8"))
if not isinstance(data, list):
    raise SystemExit("Expected a JSON array at top level.")

# Required column order from the grader
columns = ["user_id", "event_type", "timestamp", "session_id", "page_url", "duration"]

rows = []
for obj in data:
    if not isinstance(obj, dict):
        raise SystemExit("Expected each item to be a JSON object.")
    rows.append([obj.get(col, None) for col in columns])

out = {"columns": columns, "rows": rows}
OUTPUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")

print(f"Wrote {OUTPUT} with {len(columns)} columns and {len(rows)} rows")
