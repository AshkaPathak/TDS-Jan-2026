# GA8 — Q15: GCP AI Studio — Gemini JSON Data Extraction

## Problem Summary
In this question, the task was to extract structured JSON data from a paragraph and compute a verification hash from the extracted fields.

The unique paragraph assigned here was:

```text
Alice Nakamura is a 35-year-old cloud architect working at Spotify in Tokyo.
```

Final submission format:

```text
name,age,city,role,company,verify_hash
```

---

## Step-by-Step Solution

### Step 1 — Extract the Fields

The paragraph contains these fields:

| Field | Value |
|---|---|
| `name` | `Alice Nakamura` |
| `age` | `35` |
| `city` | `Tokyo` |
| `role` | `cloud architect` |
| `company` | `Spotify` |

Extracted JSON:

```json
{
  "name": "Alice Nakamura",
  "age": 35,
  "city": "Tokyo",
  "role": "cloud architect",
  "company": "Spotify"
}
```

---

### Step 2 — Compute Verify Hash

Formula:

```text
sha256(email:name:age:city:role:company)[:14]
```

Email used:

```text
23f3002663@ds.study.iitm.ac.in
```

Constructed input string:

```text
23f3002663@ds.study.iitm.ac.in:Alice Nakamura:35:Tokyo:cloud architect:Spotify
```

SHA-256 hash, first 14 hex characters:

```text
5e95630c9bbf52
```

---

## Reproducible Script

The calculation was saved in `extract_json.py`.

```python
import hashlib
import json


EMAIL = "23f3002663@ds.study.iitm.ac.in"
paragraph = "Alice Nakamura is a 35-year-old cloud architect working at Spotify in Tokyo."

data = {
    "name": "Alice Nakamura",
    "age": 35,
    "city": "Tokyo",
    "role": "cloud architect",
    "company": "Spotify",
}


def main() -> None:
    name = data["name"]
    age = int(data["age"])
    city = data["city"]
    role = data["role"]
    company = data["company"]

    verify_input = f"{EMAIL}:{name}:{age}:{city}:{role}:{company}"
    verify_hash = hashlib.sha256(verify_input.encode()).hexdigest()[:14]

    print(json.dumps(data, indent=2))
    print(f"\nParagraph: {paragraph}")
    print(f"Verify input: {verify_input}")
    print(f"Verify hash: {verify_hash}")
    print(f"\nSubmit: {name},{age},{city},{role},{company},{verify_hash}")


if __name__ == "__main__":
    main()
```

Script output:

```text
{
  "name": "Alice Nakamura",
  "age": 35,
  "city": "Tokyo",
  "role": "cloud architect",
  "company": "Spotify"
}

Paragraph: Alice Nakamura is a 35-year-old cloud architect working at Spotify in Tokyo.
Verify input: 23f3002663@ds.study.iitm.ac.in:Alice Nakamura:35:Tokyo:cloud architect:Spotify
Verify hash: 5e95630c9bbf52

Submit: Alice Nakamura,35,Tokyo,cloud architect,Spotify,5e95630c9bbf52
```

---

## Final Submission

```text
Alice Nakamura,35,Tokyo,cloud architect,Spotify,5e95630c9bbf52
```

---

## Conclusion

The paragraph clearly identifies Alice Nakamura as a 35-year-old cloud architect working at Spotify in Tokyo. The extracted fields and verification hash satisfy the required submission format.
