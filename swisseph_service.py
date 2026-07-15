import os
from datetime import datetime

import swisseph as swe

from planetary_positions import get_sign
from house_engine import get_houses
from planet_house_mapper import get_planet_house
from house_lords import get_house_lords

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

    hour = dt.hour + dt.minute / 60
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

    house_longitudes = houses[0]
    ascendant = houses[1][0]

    sun = swe.calc_ut(jd, swe.SUN)[0][0]
    moon = swe.calc_ut(jd, swe.MOON)[0][0]
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

        "houses": get_houses(houses),

"house_lords": get_house_lords(get_houses(houses)),

        "planets": {

    "Sun": {
        **get_sign(sun),
        "house": get_planet_house(sun, house_longitudes)
    },

    "Moon": {
        **get_sign(moon),
        "house": get_planet_house(moon, house_longitudes)
    },

    "Mercury": {
        **get_sign(mercury),
        "house": get_planet_house(mercury, house_longitudes)
    },

    "Venus": {
        **get_sign(venus),
        "house": get_planet_house(venus, house_longitudes)
    },

    "Mars": {
        **get_sign(mars),
        "house": get_planet_house(mars, house_longitudes)
    },

    "Jupiter": {
        **get_sign(jupiter),
        "house": get_planet_house(jupiter, house_longitudes)
    },

    "Saturn": {
        **get_sign(saturn),
        "house": get_planet_house(saturn, house_longitudes)
    },

    "Rahu": {
        **get_sign(rahu),
        "house": get_planet_house(rahu, house_longitudes)
    },

    "Ketu": {
        **get_sign(ketu),
        "house": get_planet_house(ketu, house_longitudes)
     }

    }
}
