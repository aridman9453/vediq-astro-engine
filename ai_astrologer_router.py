from fastapi import APIRouter
from pydantic import BaseModel

from ai_astrologer_engine import ask_ai_astrologer
from birth_chart import generate_birth_chart

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

    birth_chart = generate_birth_chart(
        birth_date=data.birth_chart["dob"],
        birth_time=data.birth_chart["tob"],
        latitude=27.13,
        longitude=81.95,
        timezone=5.5
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
