from typing import Dict


def analyze_health(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    score = 50

    risks = []
    strengths = []

    sun = planets["Sun"]
    moon = planets["Moon"]
    mars = planets["Mars"]
    saturn = planets["Saturn"]
    mercury = planets["Mercury"]
    jupiter = planets["Jupiter"]

    sixth_house = houses[5]
    eighth_house = houses[7]
    twelfth_house = houses[11]

    # Sun
    if sun["strength"] == "Own Sign":
        score += 15
        strengths.append("Strong immunity")

    elif sun["strength"] == "Debilitated":
        score -= 10
        risks.append("Low vitality")

    # Moon
    if moon["strength"] == "Own Sign":
        score += 10
        strengths.append("Stable mental health")

    elif moon["strength"] == "Debilitated":
        score -= 8
        risks.append("Emotional stress")

    # Jupiter
    if jupiter["strength"] == "Own Sign":
        score += 10
        strengths.append("Good recovery ability")

    # Saturn
    if saturn["strength"] == "Debilitated":
        score -= 8
        risks.append("Chronic health issues")

    # Mars
    if mars["strength"] == "Debilitated":
        score -= 8
        risks.append("Inflammation / injuries")

    # Mercury
    if mercury["strength"] == "Debilitated":
        score -= 5
        risks.append("Nervous system imbalance")

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    if score >= 90:
        overall = "Excellent"

    elif score >= 75:
        overall = "Very Good"

    elif score >= 60:
        overall = "Good"

    else:
        overall = "Needs Attention"

    return {
        "health_score": score,
        "overall_health": overall,
        "6th_house_sign": sixth_house["sign"],
        "8th_house_sign": eighth_house["sign"],
        "12th_house_sign": twelfth_house["sign"],
        "strengths": strengths,
        "health_risks": risks
    }
