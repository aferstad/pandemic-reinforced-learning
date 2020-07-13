import src.constants as constants


class InfectionManager:
    def __init__(self, controller, infection_deck):
        self.__infection_rate_ladder = constants.INFECTION_RATE_LADDER
        self.__current_infection_rate = self.__infection_rate_ladder.pop(0)
        self.__n_outbreaks = 0
        self.controller = controller
        self.infection_deck = infection_deck
        self.__initial_cities_infected = False
        self.__cubes_per_color = constants.CUBES_PER_COLOR  # dict with color key and n_cube value
        self.__current_infection_card = None

    def get_current_infection_rate(self):
        return self.__current_infection_rate

    def infect_initial_cities(self):
        if self.__initial_cities_infected:
            raise ValueError('Initial Cities Already Infected!')

        for i in range(1, 4):
            cards = self.infection_deck.draw_n_cards(3)
            for card in list(cards.values()):
                city = card.get_city()
                color = city.get_color()
                city.add_cubes(n=i, color=color)
                self.__cubes_per_color[color] -= i

        self.__initial_cities_infected = True

    def infect_city(self, city, color, cubes_to_add=1):
        """
        :param city: city to add cubes to
        :param color: color of cubes to add
        :param cubes_to_add: number of cubes to add
        """
        if cubes_to_add > self.__cubes_per_color[color]:
            self.controller.game_over(reason='NO MORE CUBES')
        if city.get_n_cubes(color=color) + cubes_to_add > constants.MAX_CUBES_PER_COLOR_IN_CITY:
            if city not in self.infection_deck.cities_with_outbreaks_due_to_current_card:
                self.infection_deck.cities_with_outbreaks_due_to_current_card[city.get_name()] = city
                self.do_outbreak(city, color)
        else:
            city.add_cubes(n=cubes_to_add, color=color)

    def do_epidemic_spread(self):
        card = self.infection_deck.draw_bottom_card()
        self.infect_city(city=card.get_city,
                         color=card.get_color(),
                         cubes_to_add=constants.CUBES_TO_ADD_WHEN_EPIDEMIC)
        self.infection_deck.shuffle_discarded_cards_and_put_on_top()
        self.__current_infection_rate = self.__infection_rate_ladder.pop(0)

    def do_outbreak(self, city, color):
        """
        when a chain reaction outbreak occurs,
        do not add cubes to cities that have already
        had an outbreak as part of resolving
        the *current* infection card
        :param city: where there is outbreak
        :param color: color of the outbreak
        :return:
        """
        self.__n_outbreaks += 1
        if self.__n_outbreaks == constants.OUTBREAK_LIMIT:
            self.controller.game_over('TOO MANY OUTBREAKS')

        for adjacent_city in list(city.get_adjacent_cities.values()):
            self.infect_city(city=adjacent_city,color=color, cubes_to_add=1)

