import swisseph as swe
import os
from datetime import datetime
from planetary_positions import get_sign

EPHE_PATH = os.path.join(os.path.dirname(__file__), "ephe")
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

    mercury = swe.calc_ut(jd, swe.MERCURY)[0][0]
venus = swe.calc_ut(jd, swe.VENUS)[0][0]
mars = swe.calc_ut(jd, swe.MARS)[0][0]
jupiter = swe.calc_ut(jd, swe.JUPITER)[0][0]
saturn = swe.calc_ut(jd, swe.SATURN)[0][0]
rahu = swe.calc_ut(jd, swe.MEAN_NODE)[0][0]
ketu = (rahu + 180) % 360
return {
    "success": True,
    "julian_day": round(jd, 6),

    "ascendant": get_sign(ascendant),

    "planets": {
    "Sun": get_sign(sun),
    "Moon": get_sign(moon),
    "Mercury": get_sign(mercury),
    "Venus": get_sign(venus),
    "Mars": get_sign(mars),
    "Jupiter": get_sign(jupiter),
    "Saturn": get_sign(saturn),
    "Rahu": get_sign(rahu),
    "Ketu": get_sign(ketu)
    }
}
