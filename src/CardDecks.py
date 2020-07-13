from random import random, randint
from src.card import Card


class CardDeck:

    def __init__(self, cards):
        self.__cards = cards

        # card order is an array of strings
        self.__card_order = list(cards.keys())
        # randomly shuffles the order of strings in __card_order
        random.shuffle(self.__card_order)

    def get_card_count(self):
        return len(self.__cards)

    def draw_n_cards(self, n):
        """
        :param n: number of cards to draw
        :return: dictionary of n cards, keyed on card.str
        """
        if len(self.__cards) < n:
            raise ValueError('Not possible to draw more cards than left in deck')
        if n <= 0:
            raise ValueError('Not possible to draw 0 or less cards')

        drawn_cards = {}

        for i in range(n):
            card_str = self.__card_order.pop(0)  # pop removes element and returns it
            card = self.__cards.pop(card_str)
            drawn_cards[card_str] = card

        return drawn_cards


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

    def __init__(self, cards):
        super().__init__(cards=cards)
        self.__epidemic_cards_added = False

    def add_epidemic_cards(self, n):
        """
        After giving initial starting cards to players,
        divide the remaining player cards into n stacks,
        as equal in size as possible.
        Shuffle 1 epidemic card into each pile,
        place smaller piles on bottom.
        :param n: number of epidemic cards to add
        :return ValueError if epidemic cards have already been added, or n<=0
        """
        if self.__epidemic_cards_added:
            raise ValueError('Epidemic Cards already added!')
        if n <= 0:
            raise ValueError('Not allowed to add 0 or less epidemic cards')

        # Calculate stack sizes:
        n_cards_after_insertion = self.get_card_count() + n
        cards_in_smaller_piles = n_cards_after_insertion // n
        surplus = n_cards_after_insertion % n
        n_small_piles = n - surplus
        n_big_piles = surplus
        cards_in_bigger_piles = cards_in_smaller_piles + 1

        # Initialize variables to use in loops:
        interval_end = self.get_card_count() - 1
        current_epidemic_card_number = n

        # Insert epidemic cards by starting at end of card_order and moving to front
        for i in range(n_small_piles):
            interval_start = interval_end - cards_in_smaller_piles + 2
            index_of_epidemic_card = randint(interval_start, interval_end)  # returns random integer in range [a, b], including both end points.

            epidemic_name = 'epidemic_number_' + str(current_epidemic_card_number)
            self.__card_order.insert(index_of_epidemic_card, epidemic_name)
            self.__cards[epidemic_name] = Card(name=epidemic_name)

            current_epidemic_card_number -= 1
            interval_end = interval_start - 1

        for i in range(n_big_piles):
            interval_start = interval_end - cards_in_bigger_piles + 2
            index_of_epidemic_card = randint(interval_start, interval_end)

            epidemic_name = 'epidemic_number_' + str(current_epidemic_card_number)
            self.__card_order.insert(index_of_epidemic_card, epidemic_name)
            self.__cards[epidemic_name] = Card(name=epidemic_name)

            current_epidemic_card_number -= 1
            interval_end = interval_start - 1

        self.__epidemic_cards_added = True