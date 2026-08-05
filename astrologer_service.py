from astrologer_schema import Astrologer

ASTROLOGERS = [
    Astrologer(
        id="astro_001",
        name="Acharya Dev Sharma",
        experience=18,
        languages=["English","Hindi"],
        expertise=[
            "Career",
            "Marriage",
            "Finance",
            "Health"
        ],
        rating=4.9,
        total_reviews=382,
        price=499,
        about="Expert in Vedic Astrology and Career Guidance.",
        is_online=True
    )
]

def get_all_astrologers():
    return ASTROLOGERS

def get_astrologer(id: str):
    for astro in ASTROLOGERS:
        if astro.id == id:
            return astro
    return None
