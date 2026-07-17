import swisseph as swe

NAKSHATRA_LORDS = [
    "Ketu",
    "Venus",
    "Sun",
    "Moon",
    "Mars",
    "Rahu",
    "Jupiter",
    "Saturn",
    "Mercury"
]

DASHA_YEARS = {
    "Ketu": 7,
    "Venus": 20,
    "Sun": 6,
    "Moon": 10,
    "Mars": 7,
    "Rahu": 18,
    "Jupiter": 16,
    "Saturn": 19,
    "Mercury": 17
}


def get_vimshottari_dasha(moon_longitude):

    nakshatra = int(moon_longitude / (13 + 20 / 60))

    lord = NAKSHATRA_LORDS[nakshatra % 9]

    return {
        "current_mahadasha": lord,
        "duration_years": DASHA_YEARS[lord]
    }
