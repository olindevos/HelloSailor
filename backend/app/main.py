from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

from app.routes import stats, oauth  # ← onze routers

app = FastAPI()

# CORS (mag later strenger)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

# Routers registreren
app.include_router(stats.router)
app.include_router(oauth.router)
