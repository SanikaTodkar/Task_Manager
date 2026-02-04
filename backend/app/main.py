from fastapi import FastAPI

app = FastAPI(title="Task Management API", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "Backend is running"}