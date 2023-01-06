#Higher or Lowec Game

import random
import os
from high_low_art import logo, vs
from high_low_data import data

#function to clear console
def clear():
    os.system("clear")

#keep score
score = 0
#continue or quit game after lose
keep_playing = True
#continue if win
win_streak = True
#variable to hold A celeb
a = 0

#function to pick celeb
def pick_celeb(previous):
    while True:
        celeb = random.randint(0,len(data) - 1)
        if celeb != previous:
            return celeb

while keep_playing:
    while win_streak:
        #select 
        print(logo)





