from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from timezonefinder import TimezoneFinder
from swisseph_service import generate_birth_chart as calculate_birth_chart
from location_service import birth_datetime_to_utc

router = APIRouter(
    prefix="/birth-chart",
    tags=["Birth Chart"]
)

tf = TimezoneFinder()

class BirthChartRequest(BaseModel):
    name: str
    birth_date: str
    birth_time: str
    latitude: float
    longitude: float

@router.get("/status")
def status():
    return {"status": "Birth Chart Engine Ready"}

@router.post("/generate")
def generate(data: BirthChartRequest):
    timezone_name = tf.timezone_at(lat=data.latitude, lng=data.longitude)
    if timezone_name is None:
        raise HTTPException(status_code=400, detail="Could not find timezone for this location")

    utc_dt = birth_datetime_to_utc(
        birth_date=data.birth_date,
        birth_time=data.birth_time,
        timezone_name=timezone_name
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
