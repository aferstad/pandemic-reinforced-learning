import city_card
# import city
# import initialize_cities
# import constants

def initialize_city_cards(cities):
    cards = []
    for city in cities:
        c_card = city_card.city_card(city)
        cards.append(c_card)
    return(c_card)

# cities = initialize_cities.initialize_cities(constants.CITY_JSON_PATH)
# initialize_city_cards(cities)
