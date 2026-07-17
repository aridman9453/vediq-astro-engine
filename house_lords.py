RASHI_LORDS = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter"
}


def get_house_lords(houses):

    result = []

    for house in houses:
        print("HOUSE DATA:", house)

        if "sign" not in house:
            raise Exception(f"House missing sign: {house}")

        sign = house["sign"]

        result.append({
            "house": house["house"],
            "sign": sign,
            "lord": RASHI_LORDS[sign]
        })

    return result
