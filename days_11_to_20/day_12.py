#Day 12

#Number guessing game

import random
from number_art import logo
import os

#difficulty settings
EASY = 10
MEDIUM = 7
HARD = 5

#game loop variable
keep_playing = True

#function to clear console
def clear():
    os.system("clear")

#function to determine if guess is higher or lower than number
def high_or_low(number, guess):
    """Takes two numbero and returns 'high' or 'low' if second is higher or lower."""
    if number > guess:
        return "low"
    else:
        return "high"

while keep_playing:
    clear()
    number = random.randint(1,100)
    print(number)
    count = 0 #counts guesses
    print(logo)
    #loop to determine difficulty
    while True:
        difficulty = input("Choose difficulty: 'easy', 'medium', or 'hard': ").lower()
        if difficulty == "easy":
            difficulty = EASY
            break
        elif difficulty == "medium":
            difficulty = MEDIUM
            break
        elif difficulty == "hard":
            difficulty = HARD
            break
        else:
            print("Invalid response")
    #loop to ensure user input is an int
    while True:
        guess = input(f"I'm thinking of a number between 1 and 100.\nYou have {difficulty} attemps to guess the number: ")
        if guess.isdigit():
            guess = int(guess)
            count += 1
            break
        else:
            print("Invalid input")
    #check guess against number
    if guess == number:
        print(f"You win! The number was {number}. You got it in {count} try! ")
        play_again = input("Type 'yes' to play again, or 'no' to quit: ").lower()
        if  play_again != "yes":
            keep_playing = False
            break
    else:
        print(f"You're guess was too {high_or_low(number, guess)}.")
        while difficulty > count:
            if (difficulty - count) > 1:
                guess = input(f"You have {difficulty - count} attemps to guess the number: ")
                if guess.isdigit():
                    guess = int(guess)
                    count += 1
                    if guess == number:
                        print(f"You win! The number was {number}. You got it in {count} tries! ")
                        play_again = input("Type 'yes' to play again, or 'no' to quit: ").lower()
                        if  play_again != "yes":
                            keep_playing = False
                            break
                    else:
                        print(f"You're guess was too {high_or_low(number, guess)}.")
                else:
                    print("Invalid input")
            elif (difficulty - count) == 1:
                guess = input(f"You only have {difficulty - count} attemp left, make it count!: ")
                if guess.isdigit():
                    guess = int(guess)
                    count += 1
                    if guess == number:
                        print(f"You win! The number was {number}. You got it in {count} tries! ")
                        play_again = input("Type 'yes' to play again, or 'no' to quit: ").lower()
                        if  play_again != "yes":
                            keep_playing = False
                            break
                    else:
                        print(f"You lose! The number was {number}. Better luck next time! ")
                        play_again = input("Type 'yes' to play again, or 'no' to quit: ").lower()
                        if  play_again != "yes":
                            keep_playing = False
                            break

        
    