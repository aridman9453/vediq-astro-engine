from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase_client import supabase

router = APIRouter(prefix="/auth", tags=["Authentication"])


class SignupRequest(BaseModel):
    email: str
    password: str
    full_name: str


@router.get("/status")
def auth_status():
    return {
        "status": "Authentication module ready"
    }


@router.post("/signup")
def signup(data: SignupRequest):
    try:
        response = supabase.auth.sign_up(
            {
                "email": data.email,
                "password": data.password,
                "options": {
                    "data": {
                        "full_name": data.full_name
                    }
                }
            }
        )

        return {
            "success": True,
            "user": response.user
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
