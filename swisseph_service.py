swe.set_ephe_path(EPHE_PATH)


def check_swisseph():
    return {
        "status": "Swiss Ephemeris Loaded",
        "path": EPHE_PATH
    }


def generate_birth_chart(
    birth_date,
    birth_time,
    latitude,
    longitude,
    timezone
):
    dt = datetime.strptime(
        f"{birth_date} {birth_time}",
        "%Y-%m-%d %H:%M"
    )

    hour = dt.hour + (dt.minute / 60.0)

    utc_hour = hour - timezone

    jd = swe.julday(
        dt.year,
        dt.month,
        dt.day,
        utc_hour
    )

    houses = swe.houses(
        jd,
        latitude,
        longitude,
        b'P'
    )

    ascendant = houses[1][0]

    import swisseph as swe
import os
from datetime import datetime
from planetary_positions import get_sign

EPHE_PATH = os.path.join(os.path.dirname(__file__), "ephe")
swe.set_ephe_path(EPHE_PATH)


def check_swisseph():
    return {
        "status": "Swiss Ephemeris Loaded",
@@ -59,3 +107,14 @@ def generate_birth_chart(
        "Moon": get_sign(moon)
    }
}
    return {
    "success": True,
    "julian_day": round(jd, 6),

    "ascendant": get_sign(ascendant),

    "planets": {
        "Sun": get_sign(sun),
        "Moon": get_sign(moon)
    }
}
