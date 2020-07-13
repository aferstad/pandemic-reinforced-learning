from random import random


class CardDeck:

    def __init__(self, cards):
        self.__cards = cards

        # card order is an array of strings
        self.__card_order = list(cards.keys())
        # shuffle randomly shuffles the order of strings in __card_order
        self.shuffle()

    def get_card_count(self):
        return len(self.__cards)

    def shuffle(self):
        random.shuffle(self.__card_order)

    def draw_top_card(self):
        if len(self.__cards) == 0:
            raise ValueError('No more cards in deck')

        card_str = self.__card_order.pop(0)  # pop removes element and returns it
        card = self.__cards.pop(card_str)

        return card


class InfectionCardDeck(CardDeck):

    def shuffle_discarded_cards_and_put_on_top(self, discarded_cards):
        discarded_card_order = list(discarded_cards.keys())
        random.shuffle(discarded_card_order)

        new_order = discarded_card_order
        new_order.extend(self.__card_order)
        self.__card_order = new_order

        # 'update' inserts 'discarded_cards' dict into 'cards' dict:
        self.__cards.update(discarded_cards)

    def draw_bottom_card(self):
        if len(self.__cards) == 0:
            raise ValueError('No more cards in deck')

        card_str = self.__card_order.pop(-1)  # pop removes element and returns it
        card = self.__cards.pop(card_str)

        return card


class PlayerCardDeck(CardDeck):

    def add_epidemic_cards(self, n):
        """
        :param n: number of epidemic cards to add
        """



