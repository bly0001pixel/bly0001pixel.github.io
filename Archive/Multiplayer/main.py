import copy
import random

original_deck = [[suit, value] for suit in ['h', 'd', 'c', 's'] for value in range(1, 14)]
hands = []

def shuffle(deck):
    unshuffled_deck = copy.copy(deck)
    shuffled_deck = []
    for i in range(len(deck)):
        j = random.randint(0, len(unshuffled_deck)-1)
        shuffled_deck.append(unshuffled_deck[j])
        unshuffled_deck.remove(unshuffled_deck[j])

    return shuffled_deck

