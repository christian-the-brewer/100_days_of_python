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
