from typing import Dict


def analyze_marriage(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    score = 50

    timing = "Average"

    indicators = []

    venus = planets["Venus"]
    jupiter = planets["Jupiter"]
    mars = planets["Mars"]
    moon = planets["Moon"]
    saturn = planets["Saturn"]

    seventh_house = houses[6]
    seventh_lord = house_lords[6]["lord"]

    # Venus
    if venus["strength"] == "Own Sign":
        score += 20
        indicators.append("Strong romantic life")

    elif venus["strength"] == "Debilitated":
        score -= 10

    # Jupiter
    if jupiter["strength"] == "Own Sign":
        score += 15
        indicators.append("Supportive spouse")

    # Moon
    if moon["strength"] == "Own Sign":
        score += 10
        indicators.append("Emotional compatibility")

    # Saturn
    if saturn["strength"] == "Own Sign":
        score += 5
        indicators.append("Stable long-term marriage")

    # Mars (basic Manglik indicator)
    if mars["house"] in [1, 4, 7, 8, 12]:
        score -= 10
        indicators.append("Manglik influence detected")

    # Marriage timing
    if score >= 85:
        timing = "Early and favorable"

    elif score >= 70:
        timing = "Favorable"

    elif score >= 55:
        timing = "Slight delay possible"

    else:
        timing = "Delayed marriage likely"

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return {
        "marriage_score": score,
        "marriage_timing": timing,
        "7th_house_sign": seventh_house["sign"],
        "7th_lord": seventh_lord,
        "indicators": indicators
    }
