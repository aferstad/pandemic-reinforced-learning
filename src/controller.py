from src.player import Player
from src.init import initialize_cities
import src.constants as constants
from src.card import Card, CityCard
from src.CardDecks import InfectionCardDeck, PlayerCardDeck
from src.infectionManager import InfectionManager


class Controller:
    def __init__(self, n_players):
        # Create dictionary of city objects, keyed on city_str
        self.cities = initialize_cities(constants.CITY_JSON_PATH)

        # Initialize start_city:
        self.start_city = self.cities[constants.START_CITY_STR]
        self.start_city.build_research_station()

        # Create card decks:
        city_cards = {}
        for city in self.cities.values():
            city_cards[city.str] = CityCard(city)
        infection_cards = city_cards.copy()
        self.player_deck = PlayerCardDeck(city_cards)
        self.infection_deck = InfectionCardDeck(infection_cards)

        # Create list of players
        self.players = []
        n_cards_per_player = constants.N_PLAYERS_VS_N_INITIAL_CARDS[n_players]
        for i in range(n_players):
            starting_cards = self.player_deck.draw_n_cards(n=n_cards_per_player)
            self.players.append(Player(cards=starting_cards,
                                       city=self.start_city,
                                       controller=self,
                                       role=None))

        self.player_deck.add_epidemic_cards(n=constants.N_EPIDEMIC_CARDS)

        self.infection_manager = InfectionManager(controller=self,
                                                  infection_deck=self.infection_deck)
        self.infection_manager.infect_initial_cities()

    def begin_play(self):
        pass



