

from player import player
from initialize_cities import initialize_cities
import constants


def __create_players(n_players):
    players = []
    for i in range(n_players):
        players.append(player(city))


class controller:

    def __init__(self, n_players):
        self.n_players = n_players

        self.cities = initialize_cities(constants.CITY_JSON_PATH)
        self.start_city = [city for city in self.cities if city.str == constants.START_CITY_STR][0]








        self.players = __create_players(n_players)


