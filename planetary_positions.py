ZODIAC_SIGNS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces"
]


def get_sign(longitude):
    sign = int(longitude // 30)
    degree = longitude % 30

    return {
        "sign": ZODIAC_SIGNS[sign],
        "degree": round(degree, 4),
        "longitude": round(longitude, 4)
    }
