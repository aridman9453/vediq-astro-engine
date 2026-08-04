from fastapi import APIRouter, HTTPException
from palm_models import PalmAnalyzeRequest
from palm_service import analyze_palm

router = APIRouter()


@router.get("/status")
def palm_status():
    return {
        "success": True,
        "service": "Palm Reading Engine",
        "status": "Ready"
    }


@router.post("/analyze")
def analyze_palm_route(request: PalmAnalyzeRequest):
    try:
        result = analyze_palm(
            user_id=request.user_id,
            image_url=request.image_url,
            birth_chart=request.birth_chart,
            question=request.question
        )

        return {
            "success": True,
            "result": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
