from fastapi import APIRouter
from pydantic import BaseModel
from swisseph_service import generate_birth_chart as calculate_birth_chart
from location_service import birth_datetime_to_utc

router = APIRouter(
    prefix="/birth-chart",
    tags=["Birth Chart"]
)

class BirthChartRequest(BaseModel):
    name: str
    birth_date: str       # 'YYYY-MM-DD'
    birth_time: str       # 'HH:MM'
    latitude: float
    longitude: float
    timezone_name: str    # e.g. 'Asia/Kolkata' — replaces float timezone

@router.get("/status")
def status():
    return {"status": "Birth Chart Engine Ready"}

@router.post("/generate")
def generate(data: BirthChartRequest):
    utc_dt = birth_datetime_to_utc(
        birth_date=data.birth_date,
        birth_time=data.birth_time,
        timezone_name=data.timezone_name
    )

    chart = calculate_birth_chart(
        birth_datetime_utc=utc_dt,
        latitude=data.latitude,
        longitude=data.longitude
    )

    return {
        "success": True,
        "name": data.name,
        "chart": chart
    }
