from fastapi import APIRouter
from pydantic import BaseModel

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
    return {
        "success": True,
        "message": "Signup endpoint created",
        "user": data
    }
