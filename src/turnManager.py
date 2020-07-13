import src.constants as constants


class TurnManager:

    def __init__(self, player, controller):
        self.player = player
        self.controller = controller
        self.__actions_left = constants.ACTIONS_PER_TURN

    def do_turn(self):
        self.__do_actions()
        self.__draw_player_cards()
        self.__draw_infection_cards()

    def __do_actions(self):
        pass
        # TODO: ACTION FOR HUMAN / AI

    def __draw_player_cards(self):
        for i in range(constants.PLAYER_CARDS_DRAWN_PER_TURN):
            if self.controller.player_deck.get_card_count() == 0:
                self.controller.game_over(reason='NO MORE PLAYER CARDS TO DRAW')

            card = list(self.controller.player_deck.draw_n_cards(1).values())[0]

            if isinstance(card, card.EpidemicCard):
                self.controller.infection_manager.do_epidemic_spread()
            else:
                self.player.cards[card.get_name()] = card

        for player in self.controller.players:
            surplus = len(player.cards) - constants.PLAYER_HAND_CARD_LIMIT
            if surplus > 0:
                player.select_cards_to_discard(surplus)

    def __draw_infection_cards(self):
        for i in range(self.controller.infection_manager.get_current_infection_rate()):
            card = list(self.controller.infection_deck.draw_n_cards(n=1).values())[0]
            self.controller.infection_manager.infect_city(city=card.get_city(), color=card.get_color())
