
from random import random


class CardDeck:

    def __init__(self, cards):
        self.__cards = cards
        self.__discarded_cards = {}

        # card order is an array of strings
        self.__card_order = list(cards.keys())
        # shuffle randomly shuffles the order of strings
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.__card_order)

    def get_card_count(self):
        return len(self.__cards)

    def draw_card(self):
        if len(self.__cards) == 0:
            raise ValueError('No more cards in deck')

        card_str = self.__card_order.pop(0) # pop removes element and returns it
        card = self.__cards.pop(card_str)

        self.__discarded_cards[card_str] = card

        # TODO: CONTINUE HERE





        # pop from dict here




