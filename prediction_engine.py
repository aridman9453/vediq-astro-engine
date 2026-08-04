from typing import Dict


def generate_prediction(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    return {
        "overall_prediction": "Positive growth phase ahead.",
        "career": "Career opportunities are likely to improve.",
        "finance": "Financial stability increases gradually.",
        "relationship": "Good period for strengthening relationships.",
        "health": "Maintain a balanced lifestyle."
    }
