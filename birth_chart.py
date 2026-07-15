from fastapi import APIRouter
from schemas import BirthChartRequest

router = APIRouter(
    prefix="/birth-chart",
    tags=["Birth Chart"]
)


@router.get("/status")
def status():
    return {
        "status": "Birth Chart Engine Ready"
    }


@router.post("/generate")
def generate_birth_chart(request: BirthChartRequest):
    return {
        "success": True,
        "message": "Birth details received successfully",
        "data": {
            "name": request.name,
            "birth_date": request.birth_date,
            "birth_time": request.birth_time,
            "latitude": request.latitude,
            "longitude": request.longitude,
            "timezone": request.timezone
        }
    }
