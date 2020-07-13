

class Card:
    def __init__(self, city):
        self.str = city.str
        self.__color = city.get_color()

    def get_color(self):
        return self.__color

