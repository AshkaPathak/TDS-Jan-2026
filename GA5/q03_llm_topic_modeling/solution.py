# /// script
# requires-python = ">=3.11"
# dependencies = ["openai", "pandas"]
# ///

import json
import pandas as pd
from collections import Counter
from openai import OpenAI

MODEL = "gpt-4o-mini"
BATCH_SIZE = 10
VALID = {"Politics", "Sports", "Technology", "Business", "Entertainment"}

client = OpenAI()

df = pd.read_csv("q-topic-modeling-llm.csv")
headlines = df["headline"].dropna().tolist()

def classify_batch(batch):
    numbered = "\n".join([f"{i+1}. {h}" for i, h in enumerate(batch)])

    prompt = f"""
Classify each news headline into exactly one of these categories:
Politics, Sports, Technology, Business, Entertainment

Definitions:
- Politics: government, legislation, elections, diplomacy
- Sports: games, tournaments, athletes, records
- Technology: software, hardware, AI, cybersecurity, research
- Business: earnings, markets, corporate news, economics
- Entertainment: movies, music, TV, celebrity, awards

Return ONLY a JSON array of category names in the same order as the headlines.
No markdown. No explanation.

Headlines:
{numbered}
""".strip()

    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[{"role": "user", "content": prompt}],
    )

    text = resp.choices[0].message.content.strip()

    labels = json.loads(text)

    if not isinstance(labels, list) or len(labels) != len(batch):
        raise ValueError(f"Bad batch output: {text}")

    for label in labels:
        if label not in VALID:
            raise ValueError(f"Invalid label '{label}' in output: {text}")

    return labels

all_labels = []

for i in range(0, len(headlines), BATCH_SIZE):
    batch = headlines[i:i+BATCH_SIZE]
    labels = classify_batch(batch)
    all_labels.extend(labels)
    print(f"Processed {i+len(batch)}/{len(headlines)}")

df["topic"] = all_labels

counts = Counter(df["topic"])
print(counts)
print("Technology count:", counts["Technology"])
