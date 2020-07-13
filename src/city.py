import src.constants as constants


class City:
    def __init__(self, name, loc, color):
        self.str = name
        self.__name = name
        self.__loc = loc
        self.__color = color

        self.__adjacent_cities = None
        self.__adjacent_cities_names = None
        self.__has_research_station = False
        self.__cubes = {col: 0 for col in constants.COLORS}

    def __str__(self):
        return "{} with {} {} cubes".format(self.__name, self.__cubes[self.__color], self.__color)

    def get_name(self):
        return self.__name

    def get_loc(self):
        return self.__loc

    def get_loc(self):
        return self.__loc

    def get_color(self):
        return self.__color

    def get_n_cubes(self, color):
        return self.__cubes[color]

    def get_adjacent_cities(self):
        return self.__adjacent_cities

    def has_research_station(self):
        return self.__has_research_station

    def set_adjacent_cities(self, adjacent_cities):
        self.__adjacent_cities = adjacent_cities
        self.__adjacent_cities_names = [c.str for c in self.__adjacent_cities]

    def build_research_station(self):
        if self.__has_research_station:
            raise ValueError("I have a research station already stupid!")
        self.__has_research_station = True

    def remove_cubes(self, n, color):
        number_cubes = self.get_n_cubes(color)
        if(number_cubes < n or n <= 0):
            raise ValueError("Invalid number of cubes removed from city")
        self.__cubes[color] -= n

    def add_cubes(self, n, color):
        if n <= 0:
            raise ValueError("Not possible to add negative or 0 amount of cubes")
        if n + self.get_n_cubes(color) > constants.MAX_CUBES_PER_COLOR_IN_CITY:
            raise ValueError("Trying to add too many cubes! Should be outbreak?")

        self.__cubes[color] += n


    def adjacent_to(self, to_city):
        if to_city.str in self.__adjacent_cities_names:
            return True
        return False
