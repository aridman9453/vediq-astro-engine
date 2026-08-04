from typing import Dict


def analyze_marriage(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    return {
        "marriage_score": 82,
        "marriage_timing": "Favorable"
    }
