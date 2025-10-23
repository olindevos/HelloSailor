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
#dit geeft aan dat wanneer de gezochte endpoint niet in main.py staat hij door moet zoeken in stats.py
app.include_router(stats.router)

#server healthcheck
@app.get("/healthz")
def healthz():
    return {"status": "ok"}

