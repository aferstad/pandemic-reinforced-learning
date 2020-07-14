CITY_JSON_PATH = "data/city_data.txt"
COLORS = ['red', 'yellow', 'black', 'blue']
DEBUG = False
START_CITY_STR = 'Atlanta'
INITIAL_INFECTIONS = [3, 2, 1]
N_PLAYERS_VS_N_INITIAL_CARDS = {
    2: 4,  # in 2 player game, each player begins with 4 cards
    3: 3,
    4: 2
}
# allowed to be 4,5, or 6 dependent on difficulty:
N_EPIDEMIC_CARDS = 6
INFECTION_RATE_LADDER = [2, 2, 2, 3, 3, 4, 4]
MAX_CUBES_PER_COLOR_IN_CITY = 3
ACTIONS_PER_TURN = 4
PLAYER_CARDS_DRAWN_PER_TURN = 2
CUBES_TO_ADD_WHEN_EPIDEMIC = 3
CUBES_PER_COLOR = dict(
    zip(
        COLORS,
        [24] * len(COLORS)
    )
)

OUTBREAK_LIMIT = 8
PLAYER_HAND_CARD_LIMIT = 7
