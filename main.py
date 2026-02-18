from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    current_time = datetime.now(timezone.utc).isoformat()
    return {"message": "Hello, World!", "current_time": current_time}


@app.get("/health")
def health():
    return {"status": "ok"}
