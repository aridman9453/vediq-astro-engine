from typing import Dict

def analyze_wealth(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    return {
        "wealth_score": 75,
        "financial_growth": "Strong"
    }
