from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from a Docker container",
        "service": os.getenv("SERVICE_NAME", "hello-docker"),
    }

@app.get("/health")
def health():
    return {"status": "ok"}
  
