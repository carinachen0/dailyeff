from fastapi import FastAPI

app = FastAPI(title="Daily Efficiency Coach API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
