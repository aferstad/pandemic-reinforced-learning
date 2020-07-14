from src.player import Player
from src.init import initialize_cities
import src.constants as constants
from src.card import Card, CityCard
from src.CardDecks import InfectionCardDeck, PlayerCardDeck
from src.infectionManager import InfectionManager
import numpy as np





class SimpleEnvironment:
    """
    In this environment,
     there is 1 player,
      1 color of cubes,
       1 cube per city,
       only move action
        and remove disease,
    """

    def __init__(self, value_error_reward=-2):
        # Create dictionary of city objects, keyed on city_str
        self.cities = initialize_cities(constants.CITY_JSON_PATH)
        self.city_strings = list(self.cities.keys())

        # Initialize start_city:
        self.start_city = self.cities[constants.START_CITY_STR]

        # Create card decks:
        city_cards = {}
        for city in self.cities.values():
            city_cards[city.str] = CityCard(city)
        infection_cards = city_cards.copy()
        self.infection_deck = InfectionCardDeck(infection_cards)

        self.player = Player(cards=None,
                             city=self.start_city,
                             controller=self,
                             role=None)

        self.infection_manager = InfectionManager(controller=self,
                                                  infection_deck=self.infection_deck)
        self.infection_manager.infect_initial_cities()
        self.__action_functions = []
        self.__action_params = []
        self.__init_actions()
        self.__disease_cured = {zip(constants.COLORS, [True] * len(constants.COLORS))}
        self.__has_cubes = 0
        self.calculate_has_cubes()

        self.VALUE_ERROR_REWARD = value_error_reward

        self.state = self.get_state()
        self.done = False
        self.n_steps = 0

    def reset(self):
        self.__init__()

    def step(self, action):
        """
        :param action: action player takes,
            is either move to city or remove cubes
        :return: new_state, reward, done, _
        """
        self.n_steps += 1
        try:
            self.__action_functions[action](self.__action_params[action])
        except ValueError:
            return self.state, self.VALUE_ERROR_REWARD, self.done

        return self.get_state(), self.get_reward(), self.done()

    def calculate_has_cubes(self):
        city_has_cubes = []
        for city_str in self.city_strings:
            if self.cities[city_str].get_n_cubes() > 0:
                city_has_cubes.append(1)
            else:
                city_has_cubes.append(0)
        self.city_has_cubes = city_has_cubes




        self.__has_cubes = [
            min(1, self.cities[city_str].get_n_cubes(color=self.cities[city_str].get_color()))
            for city_str in self.city_strings
            ]
        return self.__has_cubes

    def get_state(self):
        """
        :return: array, first elements are 0/1 whether a city has cube
            last elements are 0/1 whether player may move to city
        """
        self.calculate_has_cubes()
        available_for_travel = [int(self.player.city.adjacent_to(self.cities[other_city_string])) for other_city_string in self.city_strings]
        return self.__has_cubes + available_for_travel

    def get_reward(self):
        has_cubes = [
            min(1, self.cities[city_str].get_n_cubes(color=self.cities[city_str].get_color()))
            for city_str in self.city_strings
            ]
        if sum(has_cubes) > 0:
            return -1
        else:
            return 0

    def done(self):
        pass

    def render(self):
        pass

    def close(self):
        pass

    def disease_cured(self, color):
        return self.__disease_cured[color]

    def __init_actions(self):
        # actions in range(0, len(cities)) are to move to specified city
        self.__action_functions = [self.player.drive_or_ferry_to_city] * len(self.cities)
        self.__action_params = [self.cities[city_str] for city_str in self.city_strings]

        # last action is to treat disease
        self.__action_functions.append(self.player.treat_disease)
        self.__action_params.append(self.player.city.get_color())
