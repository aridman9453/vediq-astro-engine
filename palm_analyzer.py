from typing import Dict


def analyze_palm(image_url: str) -> Dict:
    """
    Palm Analyzer

    Input:
        image_url

    Output:
        Structured palm features.
    """

    # TODO:
    # Replace this with Gemini Vision / OpenCV later

    return {

        "hand_shape": "Earth",

        "finger_shape": "Long",

        "life_line": {
            "length": "Long",
            "depth": "Deep",
            "clarity": "Clear"
        },

        "heart_line": {
            "length": "Medium",
            "depth": "Strong",
            "curve": "Curved"
        },

        "head_line": {
            "length": "Long",
            "depth": "Strong",
            "curve": "Straight"
        },

        "fate_line": {
            "strength": "Strong",
            "visibility": "Clear"
        },

        "sun_line": {
            "strength": "Medium"
        },

        "mercury_line": {
            "strength": "Weak"
        },

        "mounts": {

            "Jupiter": "High",

            "Saturn": "Normal",

            "Sun": "High",

            "Mercury": "High",

            "Venus": "Strong",

            "Moon": "Balanced",

            "Mars": "Strong"

        }

    }
