import swisseph as swe
import os

EPHE_PATH = os.path.join(os.path.dirname(__file__), "ephe")

swe.set_ephe_path(EPHE_PATH)


def check_swisseph():
    return {
        "status": "Swiss Ephemeris Loaded",
        "path": EPHE_PATH
    }
