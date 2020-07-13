from src.city import City

class Card:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class CityCard(Card):
    def __init__(self, city):
        super().__init__(name=city.get_name())
        self.__color = city.get_color()

    def get_color(self):
        return self.__color


class EpidemicCard(Card):



class EventCard(Card):

