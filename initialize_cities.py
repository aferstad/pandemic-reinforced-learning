import constants
from city import city
def initialize_cities(path):
    f=open(path, "r")
    lines = f.readlines()
    next_adjancent = False
    cities_created = {}
    adjacents_cities = {}
    for i, line in enumerate(lines):
        if next_adjancent:
            adjacent = line.replace("'","").split(",")
            adjacent = [name.strip() for name in adjacent]

            if constants.DEBUG:
                 print(adjacent)
            next_adjancent = False

            if city_name not in cities_created.keys():
                c = city(city_name, loc, color)
                cities_created[city_name] = c
                adjacents_cities[city_name] = adjacent
        elif "name" in line:
            city_name = line.split("'")[1].strip()
            if constants.DEBUG:
                print(city_name)

        elif "loc" in line:
            loc = line.split("'")[1].split(",")
            loc[0] = float(loc[0])
            loc[1] = float(loc[1])
            if constants.DEBUG:
                print(loc)

        elif "color" in line:
            color = line.split("'")[1]
            if constants.DEBUG:
                print(color)

        elif "adjacent" in line:
            next_adjancent = True
    for c in adjacents_cities.keys():
        adjacent = adjacents_cities[c]
        adjacent = [cities_created[name] for name in adjacent]
        cities_created[c].set_adjacent_cities(adjacent)
    return cities_created.values()

# initialize_cities(constants.CITY_JSON_PATH)
