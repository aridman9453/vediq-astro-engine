def get_planet_house(planet_longitude, house_longitudes):
    for i in range(12):
        start = house_longitudes[i]
        end = house_longitudes[(i + 1) % 12]

        if start < end:
            if start <= planet_longitude < end:
                return i + 1
        else:
            if planet_longitude >= start or planet_longitude < end:
                return i + 1

    return 12
