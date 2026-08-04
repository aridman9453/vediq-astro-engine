from typing import Dict


def analyze_education(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    score = 50

    talents = []
    challenges = []

    mercury = planets["Mercury"]
    jupiter = planets["Jupiter"]
    moon = planets["Moon"]
    saturn = planets["Saturn"]
    sun = planets["Sun"]

    fifth_house = houses[4]

    # Mercury
    if mercury["strength"] == "Own Sign":
        score += 20
        talents.append("Excellent analytical ability")

    elif mercury["strength"] == "Debilitated":
        score -= 10
        challenges.append("Difficulty concentrating")

    # Jupiter
    if jupiter["strength"] == "Own Sign":
        score += 15
        talents.append("Higher education potential")

    elif jupiter["strength"] == "Debilitated":
        score -= 8
        challenges.append("Slow academic progress")

    # Moon
    if moon["strength"] == "Own Sign":
        score += 10
        talents.append("Good memory")

    elif moon["strength"] == "Debilitated":
        score -= 5
        challenges.append("Emotional distractions")

    # Saturn
    if saturn["strength"] == "Own Sign":
        score += 8
        talents.append("Disciplined learner")

    # Sun
    if sun["strength"] == "Own Sign":
        score += 5
        talents.append("Leadership in academics")

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    if score >= 90:
        level = "Excellent"

    elif score >= 75:
        level = "Very Good"

    elif score >= 60:
        level = "Good"

    else:
        level = "Average"

    return {
        "education_score": score,
        "education_level": level,
        "5th_house_sign": fifth_house["sign"],
        "talents": talents,
        "challenges": challenges
    }
