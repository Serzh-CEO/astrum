from fastapi import FastAPI

app = FastAPI(title="ASTRUM API")


@app.get("/health")
def health():
    return {"status": "ok"}
