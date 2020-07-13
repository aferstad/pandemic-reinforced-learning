from src.city import City
from src.controller import Controller
from src.card import Card


class Player:

    def __init__(self, cards, city, controller, role=None):
        """
        :param cards: dict of initial player_cards objects
        :param city: start location
        :param controller: controller object
        :param role: TBD, role of player, V2 feature
        """
        self.cards = cards
        self.role = role
        self.city = city
        self.controller = controller

    def has_card(self, card):
        """
        :param card: either card object or card_str to check if player has
        :return: true if player has card
        """
        if isinstance(card, Card):
            return card.str in self.cards  # checks if string is in dict keys
        else:
            return card in self.cards

    def discard_card(self, card):
        """
        :param card: either card object or card_str to remove from player hand
        """
        if isinstance(card, Card):
            self.cards.pop(card.str)
        else:
            self.cards.pop(card)

    # ACTIONS
    def drive_or_ferry_to_city(self, to_city):
        if not self.city.adjacent_to(to_city):
            raise ValueError("drive_or_ferry_to_city not allowed since to_city not adjacent to player.city")

        self.city = to_city

    def direct_flight(self, to_city):
        """
        :param to_city: city player wants to direct_flight to, by discarding city_card matching to_city
        :return: ValueError if to_city not in self.city_cards
        """

        if not self.has_card(to_city.str):
            raise ValueError("direct_flight not allowed since player does not have to_city card")

        self.discard_card(to_city.str)
        self.city = to_city

    def charter_flight(self, to_city):
        """
        :param to_city: discard city_card that matches the city self is in to move to any to_city
        :return: ValueError if self.city not in self.city_cards
        """

        if not self.has_card(self.city.str):
            raise ValueError("charter_flight not allowed since player does not have self.city card")

        self.discard_card(self.city.str)
        self.city = to_city

    def shuttle_flight(self, to_city):
        """
        :param to_city: travel to_city if to_city and self.city has research stations
        :return: ValueError if self.city or to_city do not have research stations
        """

        if not (to_city.has_research_station() and self.city.has_research_station()):
            raise ValueError("shuttle_flight not allowed since to_city or self.city do not both have research stations")

        self.city = to_city

    def build_research_station(self):
        """
        :return: ValueError if player does not have self.city in self.city_cards
        """

        if not self.has_card(self.city.str):
            raise ValueError("build_research_station not allowed, player does not have self.city in self.city_cards")

        self.discard_card(self.city.str)
        self.city.build_research_station()

    def treat_disease(self, color):

        if self.controller.disease_cured(color):
            self.city.remove_cubes(n=self.city.get_n_cubes(color), color=color)
        else:
            self.city.remove_cubes(n=1, color=color)

    def share_knowledge(self, other_player, give=False, take=False):
        """
        :param other_player: player in same city to give or take player_card from,
            player_card must match current city
        :param give: true if self gives card
        :param take: true if self takes card
        :return: ValueError if players not in same city,
            or player that is supposed to give does not have the card
        """
        if take and give:
            raise ValueError("share_knowledge not allowed, give and take both true")
        if self.city.str != other_player.city.str:
            raise ValueError("share_knowledge not allowed, players not in same city")
        if take:
            return other_player.share_knowledge(self, give=True)
        if not self.has_card(self.city.str):
            raise ValueError("share_knowledge not allowed, player that is giving card does not have card")

        # find city_card that matches the city the player is in:
        city_card_to_give = [city_card for city_card in self.city_cards if city_card.str == self.city.str][0]

        # give this city card to other player
        # TODO: verify that the controller checks that this player does not have more than 7 cards at the end of the turn
        other_player.city_cards.append(city_card_to_give)

        # remove the card that was given from this player
        self.city_cards = [city_card for city_card in self.city_cards if city_card.str != city_card_to_give.str]

    def discover_cure(self, color):
        """
        :param color: color to discover cure for
        :return: ValueError if cure already discovered, no research station in city, not having enough cards
        """

        if self.controller.disease_cured(color):
            raise ValueError("discover_cure not allowed, cure already discovered for this color")
        if not self.city.has_research_station():
            raise ValueError("discover_cure not allowed, no research station in this city")

        city_cards_of_color = [city_card for city_card in self.city_cards if city_card.color == color]
        if len(city_cards_of_color) < 5:
            raise ValueError("discover_cure not allowed, player has less than 5 city cards of that color")
        city_cards_to_discard = city_cards_of_color[:5]
        for city_card in city_cards_to_discard:
            self.discard_card(city_card.str)




