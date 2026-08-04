from typing import Dict


def analyze_health(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    return {
        "health_score": 85,
        "focus": [
            "Sleep",
            "Exercise",
            "Stress Management"
        ]
    }
