from fastapi import APIRouter
from pydantic import BaseModel
from swisseph_service import generate_birth_chart as calculate_birth_chart

router = APIRouter(
    prefix="/birth-chart",
    tags=["Birth Chart"]
)


class BirthChartRequest(BaseModel):
    name: str
    date: str
    time: str
    latitude: float
    longitude: float
    timezone: float


@router.get("/status")
def status():
    return {
        "status": "Birth Chart Engine Ready"
    }


@router.post("/generate")
def generate(data: BirthChartRequest):

    chart = calculate_birth_chart(
        birth_date=data.date,
        birth_time=data.time,
        latitude=data.latitude,
        longitude=data.longitude,
        timezone=data.timezone
    )

    return {
        "success": True,
        "name": data.name,
        "chart": chart
    }
