

class Card:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class CityCard(Card):
    def __init__(self, city):
        super().__init__(name=city.get_name())
        self.__color = city.get_color()
        self.__city = city

    def get_color(self):
        return self.__color

    def get_city(self):
        return self.__city

    def __str__(self):
        return "<CityCard {}, color {}>".format(self.get_name(), self.__color)


class EpidemicCard(Card):
    pass


class EventCard(Card):
    pass
