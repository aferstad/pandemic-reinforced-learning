import src.constants as constants


class InfectionManager:
    def __init__(self, controller, infection_deck):
        self.__infection_rate = constants.INITIAL_INFECTION_RATE
        self.__n_outbreaks = 0
        self.controller = controller
        self.infection_deck = infection_deck
        self.__initial_cities_infected = False

    def infect_initial_cities(self):
        if self.__initial_cities_infected:
            raise ValueError('Initial Cities Already Infected!')

        for i in range(1, 4):
            cards = self.infection_deck.draw_n_cards(3)
            for card in list(cards.values()):
                city = card.get_city()
                color = city.get_color()
                city.add_cubes(n=i, color=color)

        self.__initial_cities_infected = True


