from fastapi import APIRouter

#hier staan alle endpoints die onder "stats" vallen
# Maak een router aan voor alles onder /v1/stats
router = APIRouter(prefix="/v1/stats", tags=["stats"])

@router.get("/distance")
def get_total_distance():
    return {
        "total_m": 12450,
        "total_km": 12.45,
        "updated_at": "2025-10-23T14:00:00Z"
    }
@router.get("/walked")
def get_distance_walked():
    return{
        "total_m": 100
    }