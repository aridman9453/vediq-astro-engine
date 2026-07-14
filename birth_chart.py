from fastapi import APIRouter

router = APIRouter(prefix="/birth-chart", tags=["Birth Chart"])


@router.get("/status")
def status():
    return {
        "status": "Birth Chart Engine Ready"
    }
