import src.constants as constants
from src.city import City


def initialize_cities(path):
    f = open(path, "r")
    lines = f.readlines()
    next_adjacent = False
    cities_created = {}
    adjacent_cities = {}
    current_city_id = 0
    for i, line in enumerate(lines):
        if next_adjacent:
            adjacent = line.replace("'","").split(",")
            adjacent = [name.strip() for name in adjacent]

            if constants.DEBUG:
                 print(adjacent)
            next_adjacent = False

            if city_name not in cities_created.keys():
                c = City(city_name, loc, color, city_id=current_city_id)
                current_city_id += 1
                cities_created[city_name] = c
                adjacent_cities[city_name] = adjacent
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
            next_adjacent = True
    for c in adjacent_cities.keys():
        adjacent = adjacent_cities[c]
        adjacent = [cities_created[name] for name in adjacent]
        cities_created[c].set_adjacent_cities(adjacent)
    return cities_created

