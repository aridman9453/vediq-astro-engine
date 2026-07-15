from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/birth-chart", tags=["Birth Chart"])


class BirthChartRequest(BaseModel):
    name: str
    date: str          # YYYY-MM-DD
    time: str          # HH:MM
    latitude: float
    longitude: float
    timezone: float


@router.get("/status")
def status():
    return {
        "status": "Birth Chart Engine Ready"
    }


@router.post("/generate")
def generate_birth_chart(data: BirthChartRequest):
    return {
        "success": True,
        "message": "Birth chart request received",
        "data": {
            "name": data.name,
            "date": data.date,
            "time": data.time,
            "latitude": data.latitude,
            "longitude": data.longitude,
            "timezone": data.timezone
        }
    }
