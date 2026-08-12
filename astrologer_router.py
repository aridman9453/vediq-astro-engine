from fastapi import APIRouter, HTTPException

from astrologer_service import (
    get_all_astrologers,
    get_astrologer
)

router = APIRouter(
    prefix="/astrologers",
    tags=["Human Astrologers"]
)

@router.get("/")
def all_astrologers():
    return get_all_astrologers()

@router.get("/{astro_id}")
def astrologer_details(astro_id: str):

    astro = get_astrologer(astro_id)

    if astro is None:
        raise HTTPException(
            status_code=404,
            detail="Astrologer not found"
        )

    return astro
