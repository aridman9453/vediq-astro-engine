from fastapi import APIRouter
from pydantic import BaseModel
from swisseph_service import generate_birth_chart as calculate_birth_chart
from location_service import resolve_location, birth_datetime_to_utc

router = APIRouter(
    prefix="/birth-chart",
    tags=["Birth Chart"]
)

class BirthChartRequest(BaseModel):
    name: str
    birth_date: str
    birth_time: str
    birth_place: str

@router.get("/status")
def status():
    return {"status": "Birth Chart Engine Ready"}

@router.post("/generate")
def generate(data: BirthChartRequest):
    location = resolve_location(data.birth_place)

    utc_dt = birth_datetime_to_utc(
        birth_date=data.birth_date,
        birth_time=data.birth_time,
        timezone_name=location["timezone_name"]
    )

    chart = calculate_birth_chart(
        birth_datetime_utc=utc_dt,
        latitude=location["latitude"],
        longitude=location["longitude"]
    )

    return {
        "success": True,
        "name": data.name,
        "chart": chart
    }
