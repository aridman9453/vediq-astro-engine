from typing import Dict


def generate_career_report(chart: Dict):

    planets = chart["planets"]

    houses = chart["houses"]

    tenth_house = houses[9]
    tenth_lord = chart["house_lords"][9]["lord"]

    saturn = planets["Saturn"]

    mercury = planets["Mercury"]

    sun = planets["Sun"]

    mars = planets["Mars"]

    jupiter = planets["Jupiter"]

    moon = planets["Moon"]

    score = 50

    recommendations = []

    if saturn["strength"] == "Own Sign":
        score += 15
        recommendations.append("Government")

    if mercury["strength"] == "Own Sign":
        score += 15
        recommendations.append("Business")

    if sun["strength"] == "Own Sign":
        score += 10
        recommendations.append("Leadership")

    if mars["strength"] == "Own Sign":
        score += 10
        recommendations.append("Engineering")

    if jupiter["strength"] == "Own Sign":
        score += 10
        recommendations.append("Teaching")

    if moon["strength"] == "Own Sign":
        score += 10
        recommendations.append("Public Relations")

    if score > 100:
        score = 100

    return {

        "career_score": score,

        "career_house": tenth_house,

        "career_lord": tenth_lord,

        "best_fields": recommendations,

        "career_growth":

            "Excellent"

            if score >= 85

            else

            "Good"

            if score >= 70

            else

            "Average"

    }
