from typing import Dict


def generate_prediction(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    career = chart.get("career", {})
    wealth = chart.get("wealth", {})
    marriage = chart.get("marriage", {})
    health = chart.get("health", {})

    score = 0

    score += career.get("career_score", 50)
    score += wealth.get("wealth_score", 50)
    score += marriage.get("marriage_score", 50)
    score += health.get("health_score", 50)

    overall = score / 4

    if overall >= 90:
        phase = "Excellent Growth Phase"

    elif overall >= 75:
        phase = "Strong Positive Phase"

    elif overall >= 60:
        phase = "Steady Growth"

    else:
        phase = "Challenging Phase"

    return {

        "overall_prediction": phase,

        "overall_score": round(overall, 1),

        "career_prediction":
            career.get("career_growth", "Good"),

        "finance_prediction":
            wealth.get("financial_growth", "Stable"),

        "relationship_prediction":
            marriage.get("marriage_timing", "Average"),

        "health_prediction":
            health.get("overall_health", "Good"),

        "summary": [
            "Focus on long-term planning.",
            "Avoid impulsive decisions.",
            "Spiritual practices will enhance clarity.",
            "Career opportunities may increase gradually."
        ]
    }
