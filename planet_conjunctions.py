def get_conjunctions(planets):
    conjunctions = []

    names = list(planets.keys())

    for i in range(len(names)):
        for j in range(i + 1, len(names)):

            p1 = names[i]
            p2 = names[j]

            lon1 = planets[p1]["longitude"]
            lon2 = planets[p2]["longitude"]

            diff = abs(lon1 - lon2)

            if diff > 180:
                diff = 360 - diff

            if diff <= 8:
                conjunctions.append({
                    "planet1": p1,
                    "planet2": p2,
                    "orb": round(diff, 2)
                })

    return conjunctions
