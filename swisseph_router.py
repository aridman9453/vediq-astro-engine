from fastapi import APIRouter
from swisseph_service import check_swisseph

router = APIRouter(prefix="/swisseph", tags=["Swiss Ephemeris"])


@router.get("/status")
def status():
    return check_swisseph()
