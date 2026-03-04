from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="SDSP Control Plane")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router, prefix="/v1")
