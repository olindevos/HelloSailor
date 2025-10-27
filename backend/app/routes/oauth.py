from fastapi import APIRouter, HTTPException
import os, requests

router = APIRouter(prefix="/oauth", tags=["oauth"])

@router.get("/callback")
def strava_callback(code: str | None = None, error: str | None = None):
    if error:
        raise HTTPException(status_code=400, detail=error)
    if not code:
        raise HTTPException(status_code=400, detail="Missing 'code'")

    resp = requests.post(
        "https://www.strava.com/oauth/token",
        data={
            "client_id": os.environ["STRAVA_CLIENT_ID"],
            "client_secret": os.environ["STRAVA_CLIENT_SECRET"],
            "code": code,
            "grant_type": "authorization_code",
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    # toon alleen wat je nu nodig hebt
    return {
        "ok": True,
        "refresh_token": data.get("refresh_token"),
        "scopes": data.get("scope"),
        "athlete_id": (data.get("athlete") or {}).get("id"),
    }
