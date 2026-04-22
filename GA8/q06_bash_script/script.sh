#!/bin/bash

TARGET_DIR="models"
FILE_COUNT=5
HASHES=""

mkdir -p "$TARGET_DIR"

for i in $(seq 1 $FILE_COUNT); do
    fname="run_${i}.txt"
    touch "$TARGET_DIR/$fname"
    h=$(echo -n "$fname" | shasum -a 256 | cut -c1-8)
    HASHES="${HASHES}${h}"
done

COMBINED=$(echo -n "$HASHES" | shasum -a 256 | cut -c1-8)

echo "DIR:${TARGET_DIR}|FILES:${FILE_COUNT}|HASH:${COMBINED}"
