from fastapi import APIRouter
from pydantic import BaseModel

from ai_astrologer_engine import ask_ai_astrologer
from birth_chart import calculate_birth_chart
from location_service import resolve_location

router = APIRouter(
    prefix="/ai-astrologer",
    tags=["AI Astrologer"]
)


class AIQuestion(BaseModel):
    birth_chart: dict
    question: str
    palm_report: dict | None = None


@router.post("/ask")
def ask(data: AIQuestion):

    birth_data = data.birth_chart

    location = resolve_location(
        birth_data["place"]
    )

    calculated_chart = calculate_birth_chart(
        birth_date=birth_data["dob"],
        birth_time=birth_data["tob"],
        latitude=location["latitude"],
        longitude=location["longitude"],
        timezone=location["timezone"]
    )

    answer = ask_ai_astrologer(
        birth_chart=calculated_chart,
        user_question=data.question,
        palm_report=data.palm_report
    )

    return {
        "success": True,
        "answer": answer
    }
