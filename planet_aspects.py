def get_planet_aspects(planet, house):

    aspects = []

    # Every planet aspects the 7th house
    aspects.append(((house + 6) % 12) + 1)

    # Mars
    if planet == "Mars":
        aspects.append(((house + 3) % 12) + 1)
        aspects.append(((house + 7) % 12) + 1)

    # Jupiter
    elif planet == "Jupiter":
        aspects.append(((house + 4) % 12) + 1)
        aspects.append(((house + 8) % 12) + 1)

    # Saturn
    elif planet == "Saturn":
        aspects.append(((house + 2) % 12) + 1)
        aspects.append(((house + 9) % 12) + 1)

    return sorted(list(set(aspects)))
