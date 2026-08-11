from fastapi import APIRouter
from pydantic import BaseModel

from ai_astrologer_engine import ask_ai_astrologer
from birth_chart import calculate_birth_chart

router = APIRouter(
    prefix="/ai-astrologer",
    tags=["AI Astrologer"]
)


class AIQuestion(BaseModel):
    name: str
    dob: str
    tob: str
    latitude: float
    longitude: float
    timezone: float
    question: str
    palm_report: dict | None = None


@router.post("/ask")
def ask(data: AIQuestion):

    birth_chart = calculate_birth_chart(
        birth_date=data.dob,
        birth_time=data.tob,
        latitude=data.latitude,
        longitude=data.longitude,
        timezone=data.timezone
    )

    answer = ask_ai_astrologer(
        birth_chart=birth_chart,
        user_question=data.question,
        palm_report=data.palm_report
    )

    return {
        "success": True,
        "answer": answer
    }
