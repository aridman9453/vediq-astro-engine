from fastapi import APIRouter
from pydantic import BaseModel

from ai_astrologer_engine import ask_ai_astrologer

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

    answer = ask_ai_astrologer(
        birth_chart=data.birth_chart,
        user_question=data.question,
        palm_report=data.palm_report
    )

    return {
        "success": True,
        "answer": answer
    }
