def detect_yogas(planets):

    yogas = []

    # ----------------------------
    # Budhaditya Yoga
    # Sun + Mercury in same house
    # ----------------------------

    if planets["Sun"]["house"] == planets["Mercury"]["house"]:
        yogas.append({
            "name": "Budhaditya Yoga",
            "description": "Sun and Mercury are in the same house."
        })

    # ----------------------------
    # Gajakesari Yoga
    # Moon and Jupiter in Kendra
    # ----------------------------

    moon = planets["Moon"]["house"]
    jupiter = planets["Jupiter"]["house"]

    diff = abs(moon - jupiter)

    if diff in [0, 3, 6, 9]:
        yogas.append({
            "name": "Gajakesari Yoga",
            "description": "Moon and Jupiter form a Kendra relationship."
        })

    # ----------------------------
    # Chandra Mangal Yoga
    # ----------------------------

    if planets["Moon"]["house"] == planets["Mars"]["house"]:
        yogas.append({
            "name": "Chandra Mangal Yoga",
            "description": "Moon and Mars occupy the same house."
        })

    # ----------------------------
    # Neecha Bhanga (basic)
    # ----------------------------

    for planet in planets:

        if planets[planet]["strength"] == "Debilitated":

            yogas.append({
                "name": "Neecha Planet",
                "description": f"{planet} is debilitated."
            })

    # ----------------------------
    # Vipareeta Raja Yoga
    # Dusthana Lords in Dusthana
    # (basic placeholder)
    # ----------------------------

    yogas.append({
        "name": "Vipareeta Raja Yoga",
        "description": "Detailed calculation coming in advanced version."
    })

    return yogas
