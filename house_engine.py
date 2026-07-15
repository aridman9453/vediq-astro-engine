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
        result.append({
            "house": i + 1,
            "name": HOUSE_NAMES[i],
            "longitude": round(houses[0][i], 4)
        })

    return result
