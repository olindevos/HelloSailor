from fastapi import APIRouter, HTTPException
import os, requests

router = APIRouter(prefix="/v1/strava", tags=["strava"])

STRAVA_TOKEN_URL = "https://www.strava.com/oauth/token"
STRAVA_API = "https://www.strava.com/api/v3"

def _get_access_token() -> str:
    """Ruil refresh_token in voor een kortlevend access_token."""
    try:
        resp = requests.post(
            STRAVA_TOKEN_URL,
            data={
                "client_id": os.environ["STRAVA_CLIENT_ID"],
                "client_secret": os.environ["STRAVA_CLIENT_SECRET"],
                "grant_type": "refresh_token",
                "refresh_token": os.environ["STRAVA_REFRESH_TOKEN"],
            },
            timeout=15,
        )
        if not resp.ok:
            try:
                detail = resp.json()
            except Exception:
                detail = resp.text
            raise HTTPException(status_code=resp.status_code, detail=detail)
        return resp.json()["access_token"]
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"refresh failed: {e}")

@router.get("/ping")
def strava_ping():
    """
    Haal je athlete-profiel op als rooktest.
    Bewijst dat refresh->access werkt en dat Strava antwoorden geeft.
    """
    token = _get_access_token()
    try:
        # haal basisprofiel
        me = requests.get(
            f"{STRAVA_API}/athlete",
            headers={"Authorization": f"Bearer {token}"},
            timeout=15,
        )
        if not me.ok:
            try:
                detail = me.json()
            except Exception:
                detail = me.text
            raise HTTPException(status_code=me.status_code, detail=detail)

        # optioneel: tel 1 recente activiteit (rooktest)
        acts = requests.get(
            f"{STRAVA_API}/athlete/activities?per_page=1",
            headers={"Authorization": f"Bearer {token}"},
            timeout=15,
        )
        count_hint = 0 if not acts.ok else len(acts.json())

        data = me.json()
        return {
            "ok": True,
            "athlete_id": data.get("id"),
            "username": data.get("username"),
            "firstname": data.get("firstname"),
            "lastname": data.get("lastname"),
            "sample_activities_returned": count_hint,
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"api call failed: {e}")
