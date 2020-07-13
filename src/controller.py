

from src.player import player
from src.initialize_cities import initialize_cities
import src.constants
from src.card import Card


def __create_players(n_players):
    players = []
    for i in range(n_players):
        players.append(player(city))


class Controller:

    def __init__(self, n_players):
        self.n_players = n_players

        # Create dictionary of city objects, keyed on city_str
        self.cities = initialize_cities(constants.CITY_JSON_PATH)

        # Create dictionary of card objects, keyed on city_str
        self.city_cards = {}
        for city in self.cities.values():
            self.city_cards[city.str] = card(city)
        self.infection_cards = self.city_cards.copy()





        # Initialize start_city:
        self.start_city = self.cities.get(constants.START_CITY_STR)
        self.start_city.build_research_station()









        self.players = __create_players(n_players)


