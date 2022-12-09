#Day 4
# import random
# import my_module

# random_integer = random.randint(1,10)
# print(my_module.pi)

# random_float = random.random()
# print(random_float)

# #Code Exercise Heads or Tails
# game = True

# print("Coin Toss Simulator 2022!")
# while game == True:
#     game_on = input("Press Enter to flip that coin! Enter quit or q to end the program.").lower()
#     if game_on == "quit" or game_on == "q":
#         game = False
#         break
#     else:
#         coin_toss = random.randint(1,2)
#         if coin_toss == 1:
#             print("Heads")
#         else:
#             print("Tails")

# print("Thanks for playing!")

# #lists

# states_of_america = ["Massachusetts", "New Hampshire"]
# states_of_america.append("Vermont")
# states_of_america[1] = "New New Hampshire"
# print(states_of_america)

# also_states = ["Texas", "California"]
# states_of_america.extend(also_states)
# print(states_of_america)

# #Code Exercise Banker Roulette

# import random

# print("Pay the Tab Roulette")
# names_string = input("Please enter the names of participants seperated by a comma and then a space:\n")
# names_list = names_string.split(", ")
# unlucky_winner = random.randint(1, len(names_list))
# print(f"The (un)lucky winner is...\n{names_list[unlucky_winner]}")

# #Working with lists
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes","Peaches", "Cherries", "Pears",]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# #Code Challenge Treasure Map
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = (input("Where do you want to put the treasure? "))
# x = int(position[0]) - 1
# y = int(position[1]) - 1
# map[y][x] = "x"
# print(f"{row1}\n{row2}\n{row3}")

#Rock Paper Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#variables for game control
game = True #turns to false when player quits to break loop
wins = 0 #number of times player wins
ties = 0 #number of times tied
count = 0 #count of total turns

#opening print statement with instructions
print("Rock, Paper, Scissors!\nPlay by typing rock, paper, or scissors and pressing enter. Enter quit to end the game.")
#while loop to continue playing
while game == True:
    player = input("What will you throw?\n").lower
    if player == "quit" or player == "q":
        game = False
        break
    elif player == "rock" or player == "paper" or player == "scissors":
        computer = random.randint(1,3)
        if player == "rock":
            count += 1
            print(f"You:\n{rock}\n")
            if computer == 1:
                print(f"Computer:\n{rock}\n\nIt\'s a tie!")
                ties += 1
            elif computer == 2:
                print(f"Computer:\n{paper}\n\nYou lose!")
            else:
                print(f"Computer:\n{scissors}\n\nYou win!")
                wins += 1
        elif player == "paper":
            count += 1
            print(f"You:\n{paper}\n")
            if computer == 1:
                print(f"Computer:\n{rock}\n\nYou win!")
                wins += 1
            elif computer == 2:
                print(f"Computer:\n{paper}\n\nIt\'s a tie!")
                ties += 1
            else:
                print(f"Computer:\n{scissors}\n\nYou lose!")
        else:
            count += 1
            print(f"You:\n{scissors}\n")
            if computer == 1:
                print(f"Computer:\n{rock}\n\nYou lose!")
            elif computer == 2:
                print(f"Computer:\n{paper}\n\nYou win!")
                wins += 1
            else:
                print(f"Computer:\n{scissors}\n\nIt\'s a tie!")
                ties += 1
            
    else:
        print("Please enter rock, paper, or scissors.\n")
    print(f"Wins: {wins}\nTies: {ties}\nComputer: {count -(wins + ties)}")
print(f"Thanks for playing! You won {wins} times and tied {ties} times out of {count} games.")