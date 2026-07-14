from fastapi import APIRouter

router = APIRouter(prefix="/planetary-positions", tags=["Planetary Positions"])


@router.get("/status")
def status():
    return {
        "status": "Planetary Position Engine Ready"
    }
