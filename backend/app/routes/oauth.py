from fastapi import APIRouter, HTTPException
import os, requests

router = APIRouter(prefix="/oauth", tags=["oauth"])

@router.get("/callback")
def strava_callback(code: str | None = None, error: str | None = None):
    if error:
        raise HTTPException(status_code=400, detail=error)
    if not code:
        raise HTTPException(status_code=400, detail="Missing 'code'")

    try:
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

        # ⬇️ DIT IS HET VERVANGENDE STUK
        if not resp.ok:
            try:
                payload = resp.json()
            except Exception:
                payload = None
            detail = payload or {
                "error": "strava token exchange failed",
                "status": resp.status_code,
                "reason": resp.reason,
                "body": resp.text or None,
            }
            raise HTTPException(status_code=resp.status_code, detail=detail)
        # ⬆️ TOT HIER

        data = resp.json()
        return {
            "ok": True,
            "refresh_token": data.get("refresh_token"),
            "scopes": data.get("scope"),
            "athlete_id": (data.get("athlete") or {}).get("id"),
        }

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Token exchange failed: {e}")
