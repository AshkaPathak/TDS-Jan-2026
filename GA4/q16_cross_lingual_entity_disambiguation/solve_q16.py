import json
import csv
import re

# Load entity reference
entities = []
with open("entity_reference.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        entities.append(row)

# Build lookup by canonical name
name_to_entity = {}
for e in entities:
    name_to_entity[e["canonical_name"].lower()] = e["entity_id"]

# Helper normalization
def normalize(name):
    name = name.lower()
    name = re.sub(r"[^a-z ]", "", name)
    return name.strip()

results = []

with open("documents.jsonl") as f:
    for line in f:
        doc = json.loads(line)

        doc_id = doc["doc_id"]
        mentioned = normalize(doc["mentioned_name"])

        entity_id = None

        # simple match
        for name in name_to_entity:
            if name in mentioned or mentioned in name:
                entity_id = name_to_entity[name]
                break

        # fallback
        if entity_id is None:
            entity_id = entities[0]["entity_id"]

        results.append((doc_id, entity_id))

# Write output CSV
with open("output.csv", "w") as f:
    f.write("doc_id,entity_id\n")
    for doc_id, entity_id in results:
        f.write(f"{doc_id},{entity_id}\n")

print("Generated output.csv with", len(results), "rows")
