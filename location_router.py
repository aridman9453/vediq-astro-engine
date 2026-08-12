import os
import requests
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/location",
    tags=["Location"]
)

LOCATIONIQ_KEY = os.getenv("LOCATIONIQ_API_KEY")

@router.get("/search")
def search_city(q: str):
    url = "https://api.locationiq.com/v1/autocomplete"
    params = {
        "key": LOCATIONIQ_KEY,
        "q": q,
        "limit": 5,
        "dedupe": 1
    }
    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Location search failed")

    results = response.json()
    return [
        {
            "display_name": r["display_name"],
            "lat": float(r["lat"]),
            "lon": float(r["lon"])
        }
        for r in results
    ]
