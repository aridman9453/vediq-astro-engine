from planetary_positions import get_sign

HOUSE_NAMES = [
    "1st House",
    "2nd House",
    "3rd House",
    "4th House",
    "5th House",
    "6th House",
    "7th House",
    "8th House",
    "9th House",
    "10th House",
    "11th House",
    "12th House"
]


def get_houses(houses):
    result = []

    for i in range(12):
        longitude = round(houses[0][i], 4)

        sign_data = get_sign(longitude)

        result.append({
            "house": i + 1,
            "name": HOUSE_NAMES[i],
            "longitude": sign_data["longitude"],
            "sign": sign_data["sign"],
            "degree": sign_data["degree"],
            "nakshatra": sign_data["nakshatra"],
            "pada": sign_data["pada"]
        })

    return result
