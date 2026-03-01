# GA3 — Q11: AI Video Attendee Extraction (Gemini Files API)

## Problem Summary
You are given a ~44-second attendee check-in video showing live on-screen entries. The task is to:
1. Upload the video to Gemini Files API
2. Use Gemini to extract ALL 20 attendee `{name, date}` pairs
3. Return STRICT structured JSON
4. Ensure date format is exactly `dd/mm/yyyy`
5. Submit the JSON array (Pass if ≥ 15/20 correct)

---

## Approach

We used:
- Gemini Files API (`client.files.upload`)
- File state polling until `ACTIVE`
- `models/gemini-2.5-flash`
- Structured JSON schema enforcement via `response_schema`

This ensures:
- All frames are processed
- Exactly 20 entries are returned
- Strict JSON output
- Proper date formatting

---

## Project Structure

GA3/
└── q11_ai_video_attendee_extraction_gemini/
    ├── attendee_checkin_23f3002663.webm
    ├── main.py
    └── q11_ai_video_attendee_extraction_gemini.md

---

## Installation

cd ~/TDS-Jan-2026
python3 -m venv .venv
source .venv/bin/activate
pip install google-genai

export GEMINI_API_KEY="your_key_here"

---

## main.py

import sys
import time
import json
from google import genai
from google.genai import types

def wait_until_active(client, file_name: str):
    while True:
        f = client.files.get(name=file_name)
        if f.state == "ACTIVE":
            return
        if f.state == "FAILED":
            raise RuntimeError("Video processing FAILED")
        time.sleep(2)

def upload_video(client, path: str):
    f = client.files.upload(file=path)
    wait_until_active(client, f.name)
    return f

def extract_attendees(client, video_file):
    schema = {
        "type": "ARRAY",
        "items": {
            "type": "OBJECT",
            "properties": {
                "name": {"type": "STRING"},
                "date": {"type": "STRING"}
            },
            "required": ["name", "date"]
        }
    }

    prompt = """
You are given a 44-second attendee check-in video.

Extract ALL attendee entries shown on screen.
Return STRICT JSON ARRAY ONLY (no extra text).
Each item must be:
- name: attendee full name
- date: registration date in EXACT format dd/mm/yyyy

There are 20 total entries. Return all 20.
"""

    resp = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=[video_file, prompt],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=schema
        )
    )
    return json.loads(resp.text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <video_file.webm>")
        sys.exit(1)

    video_path = sys.argv[1]
    client = genai.Client()

    print("Uploading video...")
    vf = upload_video(client, video_path)

    print("Extracting attendees...")
    data = extract_attendees(client, vf)

    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()

---

## Run Command

python main.py attendee_checkin_23f3002663.webm

---

## Extracted JSON Output (Submitted)

[
  {"name": "Samuel Gupta", "date": "17/09/2024"},
  {"name": "Stefan Tan", "date": "14/09/2024"},
  {"name": "Arjun Russo", "date": "22/02/2025"},
  {"name": "Thabo Solis", "date": "06/06/2026"},
  {"name": "Valentina Erikson", "date": "24/12/2024"},
  {"name": "James Weber", "date": "22/03/2025"},
  {"name": "Chen Lindqvist", "date": "08/04/2026"},
  {"name": "Omar Gomez", "date": "27/08/2026"},
  {"name": "Noah Hashimoto", "date": "20/02/2025"},
  {"name": "Vivek Nkosi", "date": "06/12/2026"},
  {"name": "Aditi Rahman", "date": "07/09/2024"},
  {"name": "Siddharth Suzuki", "date": "03/11/2024"},
  {"name": "Isabella Gomez", "date": "09/08/2025"},
  {"name": "Lena Kumar", "date": "20/08/2026"},
  {"name": "Gabriel Fernandez", "date": "18/12/2026"},
  {"name": "Priya Nakamura", "date": "28/10/2025"},
  {"name": "Santiago Weber", "date": "15/09/2024"},
  {"name": "Charlotte Kumar", "date": "05/12/2024"},
  {"name": "Noah Laurent", "date": "15/05/2025"},
  {"name": "Petra Schmidt", "date": "23/10/2024"}
]

## Final Result
✔ 20 attendee entries extracted  
✔ Correct dd/mm/yyyy format  
✔ Structured JSON output  
✔ Portal accepted submission  
