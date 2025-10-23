from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes import stats


app = FastAPI()

# TEMP: sta alle origins toe om de verbinding te testen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # straks beperken we dit
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.include_router(stats.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}

