#Higher or Lowec Game

import random
import os
from high_low_art import logo, vs
from high_low_data import data

#function to clear console
def clear():
    os.system("clear")

#keep score
#score = 0
#continue or quit game after lose
keep_playing = True
#continue if win
#win_streak = True
#variable to hold A celeb
a = 0

#function to pick celeb
def pick_celeb(previous):
    """Takes previous celeb and returns a different one"""
    while True:
        celeb = random.randint(0,len(data) - 1)
        if celeb != previous:
            return celeb

#function to compare followers
def compare(a, b):
    """Takes two celebs and returns the one with more followers"""
    if data[a]["follower_count"] > data[b]["follower_count"]:
        return "a"
    else:
        return "b"

while keep_playing:
    win_streak = True #continue if win
    score = 0 #keep score
    clear()
    a = pick_celeb(-1)
    while win_streak:
        clear()
        
        #select second  celeb
        b = pick_celeb(a)
        #first celeb data
        a_name = data[a]["name"]
        a_followers = data[a]["follower_count"]
        a_description = data[a]["description"].lower()
        a_country = data[a]["country"]
        #second celeb data
        b_name = data[b]["name"]
        b_followers = data[b]["follower_count"]
        b_description = data[b]["description"].lower()
        b_country = data[b]["country"]

        print(logo)
        if score > 0:
            print(f"Correct! You're score is {score}")
        print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
        print(vs)
        print(f"Against B: {b_name}, a {b_description}, from {b_country}.")
        #take user guess
        while True:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if guess == "a" or guess == "b":
                break
            else:
                print("Enter 'a' or 'b'.")

        #compare followers
        if guess == compare(a, b):
            score += 1
            a = b
        else:
            win_streak = False
            play_again = input(f"Wrong! You had a score of {score}. Play again? 'y' for yes, 'n' for no: ").lower()
            if play_again == "y":
                break
            else:
                keep_playing = False
                break

            

       

