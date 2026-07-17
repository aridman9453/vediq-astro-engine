def generate_navamsa(planets):

    navamsa = {}

    for name, data in planets.items():

        degree = data.get("degree", data["longitude"] % 30)

        navamsa[name] = {
            "navamsa_pada": int(degree / 3.333333) + 1
        }

    return navamsa
