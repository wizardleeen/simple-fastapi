import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

GREETING_NAME = os.getenv("GREETING_NAME", "World")

app = FastAPI()


@app.get("/")
def root():
    current_time = datetime.now(timezone.utc).isoformat()
    return {"message": f"Hello, {GREETING_NAME}!", "current_time": current_time}


@app.get("/health")
def health():
    return {"status": "ok"}
