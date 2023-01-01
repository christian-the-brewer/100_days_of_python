#Day 11 Blackjack Game

import os
import random

#clear
clear = lambda: os.system('cls')



#deal card 
def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #deck of cards
    card = random.choice(cards)
    return card

# deal cards to user and computer
user_cards = []
computer_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)

