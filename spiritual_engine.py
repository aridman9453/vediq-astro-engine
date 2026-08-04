from typing import Dict


def analyze_spirituality(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    score = 50

    strengths = []
    practices = []

    jupiter = planets["Jupiter"]
    ketu = planets["Ketu"]
    moon = planets["Moon"]
    saturn = planets["Saturn"]
    sun = planets["Sun"]

    ninth_house = houses[8]
    twelfth_house = houses[11]

    # Jupiter
    if jupiter["strength"] == "Own Sign":
        score += 20
        strengths.append("Strong spiritual wisdom")
        practices.append("Study of scriptures")

    # Moon
    if moon["strength"] == "Own Sign":
        score += 10
        strengths.append("Inner peace")
        practices.append("Meditation")

    # Saturn
    if saturn["strength"] == "Own Sign":
        score += 10
        strengths.append("Discipline")
        practices.append("Regular spiritual routine")

    # Sun
    if sun["strength"] == "Own Sign":
        score += 8
        practices.append("Surya Arghya")

    # Ketu
    if ketu["strength"] == "Own Sign":
        score += 15
        strengths.append("High spiritual inclination")
        practices.append("Silence & Detachment")

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    if score >= 90:
        level = "Highly Spiritual"

    elif score >= 75:
        level = "Strong"

    elif score >= 60:
        level = "Growing"

    else:
        level = "Needs Practice"

    return {
        "spiritual_score": score,
        "spiritual_level": level,
        "9th_house_sign": ninth_house["sign"],
        "12th_house_sign": twelfth_house["sign"],
        "strengths": strengths,
        "recommended_practices": practices
    }
