from typing import Dict


def analyze_career(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    score = 50
    careers = []

    sun = planets["Sun"]
    mercury = planets["Mercury"]
    mars = planets["Mars"]
    jupiter = planets["Jupiter"]
    saturn = planets["Saturn"]
    moon = planets["Moon"]

    # Sun
    if sun["strength"] == "Own Sign":
        score += 15
        careers.extend([
            "Government",
            "Administration",
            "Leadership",
            "Politics"
        ])

    # Mercury
    if mercury["strength"] == "Own Sign":
        score += 15
        careers.extend([
            "Business",
            "Finance",
            "Technology",
            "AI",
            "Software"
        ])

    # Mars
    if mars["strength"] == "Own Sign":
        score += 12
        careers.extend([
            "Engineering",
            "Defence",
            "Police",
            "Construction"
        ])

    # Jupiter
    if jupiter["strength"] == "Own Sign":
        score += 12
        careers.extend([
            "Teaching",
            "Law",
            "Consulting",
            "Spiritual Guidance"
        ])

    # Saturn
    if saturn["strength"] == "Own Sign":
        score += 12
        careers.extend([
            "Manufacturing",
            "Infrastructure",
            "Mining",
            "Real Estate"
        ])

    # Moon
    if moon["strength"] == "Own Sign":
        score += 10
        careers.extend([
            "Media",
            "Hospitality",
            "Public Relations",
            "Travel"
        ])

    # 10th House Sign
    tenth_sign = houses[9]["sign"]

    if tenth_sign == "Virgo":
        careers.extend([
            "Data Science",
            "Programming",
            "Analytics",
            "Healthcare"
        ])

    elif tenth_sign == "Leo":
        careers.extend([
            "CEO",
            "Government",
            "Politics"
        ])

    elif tenth_sign == "Capricorn":
        careers.extend([
            "Corporate",
            "Management",
            "Administration"
        ])

    elif tenth_sign == "Aquarius":
        careers.extend([
            "AI",
            "Research",
            "Innovation"
        ])

    careers = list(dict.fromkeys(careers))

    if score > 100:
        score = 100

    if score >= 90:
        growth = "Excellent"

    elif score >= 75:
        growth = "Very Strong"

    elif score >= 60:
        growth = "Good"

    else:
        growth = "Average"

    return {
        "career_score": score,
        "career_growth": growth,
        "best_fields": careers[:10]
    }
