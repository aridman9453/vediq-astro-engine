from pydantic import BaseModel
from typing import List, Optional

class Astrologer(BaseModel):
    id: str
    name: str
    photo_url: Optional[str] = None
    experience: int
    languages: List[str]
    expertise: List[str]
    rating: float
    total_reviews: int
    price: float
    about: str
    is_online: bool
