from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

# TEMP: sta alle origins toe om de verbinding te testen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # straks beperken we dit
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/v1/stats/distance")
def get_total_distance():
    return {
        "total_m": 12450,
        "total_km": 12.45,
        "updated_at": "2025-10-23T14:00:00Z"
    }