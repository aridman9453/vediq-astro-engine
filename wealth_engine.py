from typing import Dict


def analyze_wealth(chart: Dict):

    planets = chart["planets"]

    score = 50

    best_sources = []

    jupiter = planets["Jupiter"]
    venus = planets["Venus"]
    mercury = planets["Mercury"]
    saturn = planets["Saturn"]

    # Jupiter
    if jupiter["strength"] == "Own Sign":
        score += 20
        best_sources.append("Long-term Investments")

    elif jupiter["strength"] == "Neutral":
        score += 10

    # Venus
    if venus["strength"] == "Own Sign":
        score += 15
        best_sources.append("Luxury Business")

    elif venus["strength"] == "Debilitated":
        score -= 10

    # Mercury
    if mercury["strength"] == "Own Sign":
        score += 15
        best_sources.append("Trading & Business")

    # Saturn
    if saturn["strength"] == "Own Sign":
        score += 10
        best_sources.append("Real Estate")

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    if score >= 85:
        growth = "Excellent"

    elif score >= 70:
        growth = "Strong"

    elif score >= 55:
        growth = "Average"

    else:
        growth = "Needs Improvement"

    return {
        "wealth_score": score,
        "financial_growth": growth,
        "wealth_sources": best_sources
    }
