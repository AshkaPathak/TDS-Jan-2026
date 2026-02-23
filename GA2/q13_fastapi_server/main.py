from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_students():
    students = []
    with open("q-fastapi.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students.append({
                "studentId": int(row["studentId"]),
                "class": row["class"]
            })
    return students

@app.get("/api")
def get_students(class_name: str = Query(None, alias="class")):
    students = load_students()
    
    if class_name:
        students = [s for s in students if s["class"] == class_name]

    return {"students": students}

