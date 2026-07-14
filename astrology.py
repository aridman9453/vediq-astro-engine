from fastapi import APIRouter

router = APIRouter(prefix="/astrology", tags=["Astrology"])


@router.get("/status")
def status():
    return {
        "status": "Astrology Engine Ready"
    }
