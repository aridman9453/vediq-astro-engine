from typing import Dict


def generate_remedies(chart: Dict):

    planets = chart["planets"]

    remedies = []

    weak_planets = []

    for name, planet in planets.items():

        if planet["strength"] == "Debilitated":

            weak_planets.append(name)

    for planet in weak_planets:

        if planet == "Sun":

            remedies.append({
                "planet": "Sun",
                "gemstone": "Ruby",
                "mantra": "Om Hram Hrim Hraum Sah Suryaya Namah",
                "donation": "Donate wheat on Sunday",
                "fasting": "Sunday Fast",
                "color": "Red"
            })

        elif planet == "Moon":

            remedies.append({
                "planet": "Moon",
                "gemstone": "Pearl",
                "mantra": "Om Som Somaya Namah",
                "donation": "Donate Rice",
                "fasting": "Monday Fast",
                "color": "White"
            })

        elif planet == "Mars":

            remedies.append({
                "planet": "Mars",
                "gemstone": "Red Coral",
                "mantra": "Om Angarakaya Namah",
                "donation": "Red Lentils",
                "fasting": "Tuesday Fast",
                "color": "Red"
            })

        elif planet == "Mercury":

            remedies.append({
                "planet": "Mercury",
                "gemstone": "Emerald",
                "mantra": "Om Budhaya Namah",
                "donation": "Green Moong",
                "fasting": "Wednesday Fast",
                "color": "Green"
            })

        elif planet == "Jupiter":

            remedies.append({
                "planet": "Jupiter",
                "gemstone": "Yellow Sapphire",
                "mantra": "Om Brim Brihaspataye Namah",
                "donation": "Yellow Clothes",
                "fasting": "Thursday Fast",
                "color": "Yellow"
            })

        elif planet == "Venus":

            remedies.append({
                "planet": "Venus",
                "gemstone": "Diamond",
                "mantra": "Om Shukraya Namah",
                "donation": "White Sweets",
                "fasting": "Friday Fast",
                "color": "White"
            })

        elif planet == "Saturn":

            remedies.append({
                "planet": "Saturn",
                "gemstone": "Blue Sapphire",
                "mantra": "Om Sham Shanicharaya Namah",
                "donation": "Black Sesame",
                "fasting": "Saturday Fast",
                "color": "Blue"
            })

    if not remedies:

        remedies.append({
            "planet": "General",
            "gemstone": "None Required",
            "mantra": "Gayatri Mantra",
            "donation": "Food Donation",
            "fasting": "Optional",
            "color": "Yellow"
        })

    return {
        "weak_planets": weak_planets,
        "recommended_remedies": remedies
    }
