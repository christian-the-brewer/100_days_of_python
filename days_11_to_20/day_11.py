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

game_over = False

for _ in range(2):
    user_cards.append(deal_card)
    computer_cards.append(deal_card)

def calculate_score(hand):
    """Adds up hand"""

    #check for blackjack
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    for cards in hand:
        if sum(hand) > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)

    return sum(hand)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}")
print(f"computer cards: {computer_cards}")

if user_score == 0 or calculate_score == 0 or user_score > 21:
    game_over = True
