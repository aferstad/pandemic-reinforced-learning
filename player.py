# player

from city import city


class player:

    def __init__(self, city_cards, role = None, city = city, controller = controller):
        """
        :param city_cards: list of initial city_card objects
        :param role: TBD, role of player, V2 feature
        :param city: start location
        """

        self.city_cards = city_cards
        self.role = role
        self.city = city
        self.controller = controller


    def __has_city_card(self, city_card_str):
        """
        :param city_card_str: city card to check if player has in hand
        :return: true if player has card
        """
        for city_card in self.city_cards:
            if city_card.str == city_card_str:
                return True

        return False

    def __discard_city_card(self, city_card_str):
        self.city_cards = [city_card for city_card in self.city_cards if city_card.str != city_card_str]

        # TODO: change boolean in city_card that is discarded to true?


    # TURN EVENTS





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

        if not self.__has_city_card(to_city.str):
            raise ValueError("direct_flight not allowed since player does not have to_city card")

        self.__discard_city_card(to_city.str)
        self.city = to_city

    def charter_flight(self, to_city):
        """
        :param to_city: discard city_card that matches the city self is in to move to any to_city
        :return: ValueError if self.city not in self.city_cards
        """

        if not self.__has_city_card(self.city.str):
            raise ValueError("charter_flight not allowed since player does not have self.city card")

        self.__discard_city_card(self.city.str)
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

        if not self.__has_city_card(self.city.str):
            raise ValueError("build_research_station not allowed, player does not have self.city in self.city_cards")

        self.__discard_city_card(self.city.str)
        self.city.build_research_station()

    def treat_disease(self, color):

        if self.controller.disease_cured(color):
            self.city.remove_cubes(n=3, color=color)
        else:
            self.city.remove_cubes(n=1, color=color)

    def share_knowledge(self, other_player, give = False, take = False):
        """
        :param other_player: player in same city to give or take player_card from,
            player_card must match current city
        :param give: true if self gives card
        :param take: true if self takes card
        :return: ValueError if players not in same city,
            or player that is supposed to give does not have the card
        """

        

