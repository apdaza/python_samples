import random

_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def _next_card():
    return random.choice(_cards)

class Dealer():
    def __init__(self):
        self.hand = []

    def new_round(self):
        self.hand = [_next_card(), _next_card()]
