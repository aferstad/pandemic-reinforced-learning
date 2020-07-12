
from random import random


class CardDeck:

    def __init__(self, cards):
        self.__cards = cards

        # card order is an array of strings
        self.__card_order = list(cards.keys())
        # shuffle randomly shuffles the order of strings
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.__card_order)

    def get_n_cards(self):
        return len(self.__n_cards)

    def draw_card(self):
        if len(self.__n_cards) == 0:
            raise ValueError('No more cards in deck')

        names_of_cards_to_draw = self.__card_order[:n]
        cards_to_draw = self.__cards

        # pop from dict here



