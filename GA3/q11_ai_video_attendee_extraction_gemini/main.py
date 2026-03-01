import sys
import time
import json
from google import genai
from google.genai import types

def wait_until_active(client, file_name):
    while True:
        f = client.files.get(name=file_name)
        if f.state == "ACTIVE":
            return
        if f.state == "FAILED":
            raise RuntimeError("Video processing failed")
        time.sleep(2)

def upload_video(client, path):
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
Extract ALL attendee check-in entries visible in this video.

Return STRICT JSON array only.
Each item must contain:
- name (string)
- date in format dd/mm/yyyy

There should be 20 total entries.
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=[video_file, prompt],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=schema
        )
    )

    return json.loads(response.text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <video_file>")
        sys.exit(1)

    video_path = sys.argv[1]

    client = genai.Client()

    print("Uploading video...")
    video = upload_video(client, video_path)

    print("Extracting attendees...")
    attendees = extract_attendees(client, video)

    print(json.dumps(attendees, indent=2))

if __name__ == "__main__":
    main()
