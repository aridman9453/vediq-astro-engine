from typing import Dict


def generate_remedies(chart: Dict):

    planets = chart["planets"]
    houses = chart["houses"]
    house_lords = chart["house_lords"]

    return {
        "gemstone": "Yellow Sapphire",
        "mantra": "Om Brim Brihaspataye Namah",
        "donation": "Donate yellow clothes on Thursday",
        "fasting": "Thursday fasting recommended"
    }
