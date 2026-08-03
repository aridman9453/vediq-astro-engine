from palm_analyzer import analyze_palm
from palm_prompts import SYSTEM_PROMPT, build_palm_prompt

from google import genai
import os
import uuid
from datetime import datetime

from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_palm_report(
    user_id: str,
    image_url: str,
    birth_chart: dict,
    question: str = "Analyze my palm completely."
):

    # -----------------------------
    # Palm Feature Extraction
    # -----------------------------

    palm_features = analyze_palm(image_url)

    # -----------------------------
    # Build Prompt
    # -----------------------------

    prompt = build_palm_prompt(
        birth_chart=birth_chart,
        palm_data=palm_features,
        question=question
    )

    # -----------------------------
    # Gemini Response
    # -----------------------------

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=[
            SYSTEM_PROMPT,
            prompt
        ]
    )

    final_report = response.text

    # -----------------------------
    # Save Report
    # -----------------------------

    report_id = str(uuid.uuid4())

    supabase.table("palm_reports").insert({

        "id": report_id,

        "user_id": user_id,

        "image_url": image_url,

        "analysis_json": palm_features,

        "final_report": final_report,

        "created_at": datetime.utcnow().isoformat()

    }).execute()

    return {

        "success": True,

        "report_id": report_id,

        "analysis": palm_features,

        "report": final_report

    }
