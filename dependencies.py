from fastapi import Header, HTTPException
from supabase_client import supabase


def get_current_user(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")

    token = authorization.replace("Bearer ", "")

    try:
        response = supabase.auth.get_user(token)

        if response.user is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return response.user

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
