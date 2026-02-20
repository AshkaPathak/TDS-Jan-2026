from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "GA2 Q10 Docker Deployment Successful",
        "port": os.getenv("APP_PORT")
    }

