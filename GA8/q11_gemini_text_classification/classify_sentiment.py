import hashlib


EMAIL = "23f3002663@ds.study.iitm.ac.in"

sentences = [
    "The customer service was absolutely terrible and I will never return.",
    "The repair cost was outrageously expensive and the problem still is not fixed.",
    "This is the best movie I have ever seen in my entire life!",
]

labels = [
    "NEGATIVE",
    "NEGATIVE",
    "POSITIVE",
]


def main() -> None:
    total_words = 0
    total_chars = 0

    for i, (sentence, label) in enumerate(zip(sentences, labels), start=1):
        words = sentence.split()
        total_words += len(words)
        total_chars += len(sentence)
        print(f"Sentence {i}: {label} (words={len(words)}, chars={len(sentence)})")

    labels_csv = ",".join(labels)
    verify_input = f"{EMAIL}:{labels_csv}:{total_words}:{total_chars}"
    verify_hash = hashlib.sha256(verify_input.encode()).hexdigest()[:14]

    print(f"\nLabels: {labels_csv}")
    print(f"Total words: {total_words}")
    print(f"Total chars: {total_chars}")
    print(f"Verify input: {verify_input}")
    print(f"Verify hash: {verify_hash}")
    print(f"\nSubmit: {labels_csv},{total_words},{verify_hash}")


if __name__ == "__main__":
    main()
