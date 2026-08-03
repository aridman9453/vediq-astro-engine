from datetime import datetime
from supabase_client import supabase


def save_palm_reading(
    user_id: str,
    image_url: str,
    result: dict,
    language: str = "English"
):
    """
    Save completed palm reading.
    """

    data = {
        "user_id": user_id,
        "image_url": image_url,
        "language": language,
        "result": result,
        "created_at": datetime.utcnow().isoformat()
    }

    supabase.table("palm_readings").insert(data).execute()

    return True
