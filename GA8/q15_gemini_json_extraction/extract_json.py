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
