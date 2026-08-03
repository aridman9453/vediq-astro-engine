from fastapi import APIRouter, HTTPException
from palm_models import PalmAnalyzeRequest
from palm_service import analyze_palm_report

router = APIRouter(
    prefix="/palm",
    tags=["Palm Reading"]
)


@router.post("/analyze")
def analyze_palm(request: PalmAnalyzeRequest):

    try:

        report = analyze_palm_report(

            user_id=request.user_id,

            image_url=request.image_url,

            birth_chart=request.birth_chart,

            question=request.question

        )

        return report

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.get("/report/{report_id}")
def get_report(report_id: str):

    from palm_service import supabase

    result = (

        supabase

        .table("palm_reports")

        .select("*")

        .eq("id", report_id)

        .execute()

    )

    if not result.data:

        raise HTTPException(

            status_code=404,

            detail="Report not found"

        )

    return {

        "success": True,

        "report": result.data[0]

    }


@router.get("/history/{user_id}")
def history(user_id: str):

    from palm_service import supabase

    result = (

        supabase

        .table("palm_reports")

        .select("*")

        .eq("user_id", user_id)

        .order("created_at", desc=True)

        .execute()

    )

    return {

        "success": True,

        "history": result.data

    }
