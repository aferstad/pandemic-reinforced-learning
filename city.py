import json

def check_if_adjancet(self, city):
    return True


def save_dict_as_json(output_dict, output_path):
    """
    :param output_path: where to save json file
    :return: nothing, saves dict as json at output_path
    """
    with open(output_path, 'w') as outfile:
        json.dump(output_dict, outfile)


def open_dict_from_json(input_path):
    """
    :return: dict read from json at input_path
    """
    with open(input_path) as json_file:
        input_dict = json.load(json_file)
    return input_dict



class city:
    def __init__(self, name, loc, color):
        self.__name = name
        self.__loc = loc
        self.__color = color

    def get_name(self):
        return self.__name

    def get_loc(self):
        return self.__loc

    def get_loc(self):
        return self.__loc

def initialize_cities():
    f=open("city_data.txt", "r")
    lines = f.readlines()
    next_adjancent = False
    cities_created = {}
    adjacents_cities = {}
    for i, line in enumerate(lines):
        if next_adjancent:
            adjacent = line.replace("'","").split(",")
            adjacent = [name.strip() for name in adjacent]

            print(adjacent)
            next_adjancent = False

            if city_name not in cities_created.keys():
                c = city(city_name, loc, color)
                cities_created[city_name] = c
                adjacents_cities[city_name] = adjacent

        elif "name" in line:
            city_name = line.split("'")[1].replace(" ","").strip()
            print(city_name)
            state = 1

        elif "loc" in line:
            loc = line.split("'")[1].split(",")
            loc[0] = float(loc[0])
            loc[1] = float(loc[1])
            print(loc)
            state =+ 1

        elif "color" in line:
            color = line.split("'")[1]
            print(color)
            state =+ 1

        elif "adjacent" in line:
            next_adjancent = True
    for c in adjacents_cities.keys():
        if c not in cities_created.keys():
            raise ValueError("City not created, read error")
        adjacent = adjacents_cities[c]
        adjacent = [cities_created[name] for name in adjacent]


initialize_cities()
