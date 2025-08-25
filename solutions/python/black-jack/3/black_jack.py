"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card."""
    values = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }
    return values[card]

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one > value_two:
        return card_one
    if value_one < value_two:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    values_sum = value_of_card(card_one) + value_of_card(card_two)
    
    if 'A' in (card_one, card_two):
        if 21 - values_sum + 10 >= 10:
            return 1
    
    if 21 - values_sum >= 10:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    return 'A' in (card_one, card_two) and any(card in ('10', 'J', 'Q', 'K') for card in (card_one, card_two))

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    value_sum = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= value_sum <= 11
