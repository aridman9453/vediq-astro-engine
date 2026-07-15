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
