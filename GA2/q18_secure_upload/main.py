from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import csv
import io
import os

app = FastAPI()

# CORS (required)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TOKEN = "mrvvxoubprgjgqju"
MAX_SIZE = 86 * 1024  # 86 KB

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    x_upload_token_5816: str = Header(None)
):
    # 1) Authentication
    if x_upload_token_5816 != TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # 2) File type validation (by extension)
    allowed_extensions = {".csv", ".json", ".txt"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Read file bytes
    contents = await file.read()

    # 3) File size validation
    if len(contents) > MAX_SIZE:
        raise HTTPException(status_code=413, detail="File too large")

    # 4) CSV analytics
    if ext == ".csv":
        try:
            decoded = contents.decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(status_code=400, detail="CSV must be UTF-8")

        reader = csv.DictReader(io.StringIO(decoded))
        rows = list(reader)
        row_count = len(rows)
        columns = reader.fieldnames or []

        # portal expects these columns to exist in CSV
        total_value = 0.0
        category_counts = {}

        for row in rows:
            value = float(row["value"])
            total_value += value

            cat = row["category"]
            category_counts[cat] = category_counts.get(cat, 0) + 1

        return {
            "email": "23f3002663@ds.study.iitm.ac.in",
            "filename": file.filename,
            "rows": row_count,
            "columns": columns,
            "totalValue": round(total_value, 2),
            "categoryCounts": category_counts
        }

    # For .json / .txt just validate + success
    return {"message": "File validated successfully"}
