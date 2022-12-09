#Day 3

# #Code exercise Odd or Even
# number = int(input("Which number do you want to check?: "))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# #Code exercise BMI 2.0
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     bmi_adjective = "underweight"
# elif bmi < 25:
#     bmi_adjective = "a normal weight"
# elif bmi < 30:
#     bmi_adjective = "overweight"
# elif bmi < 35:
#     bmi_adjective = "obese"
# else:
#     bmi_adjective = "clinically obese"

# print(f"Your BMI is {int(bmi)}, and you are {bmi_adjective}")
# #Code Exercise Leap Year

# year = int(input("Which year do you want to check? "))
# if year % 400 == 0:
#     print("Leap year.")
# elif year % 4 == 0:
#     if year % 100 == 0:
#         print("Not a leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# #Ticket exercise
# ticket = 0

# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm?: "))
# if height >= 120:
#     age = int(input("How old are you?: "))
#     if age < 12:
#         print("Child tickets are $5.")
#         ticket += 5
#     elif age < 18:
#         print("Youth tickets are $7.")
#         ticket += 7
#     elif 45 <= age <= 55:
#         print("Wow your life is almost over, ride for free!")
#     else:
#         print("Adult tickets are $12.")
#         ticket += 12
#     while True:
#         photo_choice = input("Would you like a photo for only $3 more? y/n: ")
#         if photo_choice == "y":
#             ticket += 3
#             break
#         elif photo_choice == "n":
#             break
#         else:
#             print("Please enter y or n: ")
#     print(f"Your total comes to ${ticket}.")
# else:
#     print("Sorry, but the minimum height to ride is 120cm.")

# #Coding Exercise Pizza Ordering
# #small pizza = 15 medium = 20 large = 25
# #pepperoni for s = 2  m/l = 3
# #extra cheese = 1

# total = 0
# pepperoni = 0
# cheese = 1
# print("Python Pizza")

# while True:
#     size = input("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\nWhich size? S, M, or L?: ")
#     if size == "S" or size == "s":
#         pepperoni = 2
#         total += 15
#         break
#     elif size == "M" or size == "m":
#         pepperoni = 3
#         total += 20
#         break
#     elif size == "L" or size == "l":
#         pepperoni = 3
#         total += 25
#         break
#     else:
#         print("Please enter S, M, or L: ")

# while True:
#     add_pepperoni = input(f"Would you like to add pepperoni for ${pepperoni}? Y/N: ")
#     if add_pepperoni == "Y" or  add_pepperoni == "y":
#         total += pepperoni
#         break
#     elif add_pepperoni == "N" or add_pepperoni == "n":
#         break
#     else:
#         print("Please enter Y or N: ")

# while True:
#     extra_cheese = input(f"Would you like to add extra cheese for ${cheese}? Y/N: ")
#     if extra_cheese == "Y" or extra_cheese == "y":
#         total += cheese
#         break
#     elif extra_cheese == "N" or extra_cheese == "n":
#         break
#     else:
#         print("Please enter Y or N: ")
# print(f"Your final bill is ${total}")


# #Code exercise Love Calculator

# first = input("Love Calculator\nEnter your name: ").lower()
# second = input("Enter your partner's name: ").lower()
# name = first + second
# true_count = name.count("t") + name.count("r") + name.count("u") + name.count("e")
# love_count = name.count("l") + name.count("o") + name.count("v") + name.count("e")
# score = str(true_count) + str(love_count)
# if score == "00":
#     print("Your score is 0, you go together like coke and mentos.")
# elif int(score) < 10 or int(score) > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif 40 <= int(score) <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}")

#Treasure Island Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

game = True

while game == True:
    stage_1 = input("You see a fork in the road before you, do you go left or right?\n").lower()
    if stage_1 == "left" or stage_1 == "l":
        print("You walk down a spooky forest road.")
        break
    elif stage_1 == "right" or stage_1 == "r":
        game = False
        print("You trip into a hidden trap in the ground and fall into a hole. Game over.")
        break
    else:
        print("Do you go left or right?\n")
while game == True:
    stage_2 = input("You come to a wide river. You think you could swim across it, or perhaps you should wait for a passing boat to carry you across. Do you wait or swim?\n").lower()
    if stage_2 == "wait" or stage_2 == "w":
        print("After a few hours of waiting a friendly fisherman offers you a ride across the river in exchange for a story.")
        break
    elif stage_2 == "swim" or stage_2 == "s":
        game = False
        print("You make it halfway before you are set upon by a school of river trout. Game over.")
        break
    else:
        print("Do you wait or swim?\n")
while game == True:
    stage_3 = input("You see ahead of you three mystical doors, set into thin air. You inspect each and see nothing out of the usual about either, except that they are simply standing on the ground, held upright by some invisible force. One is red, another yellow, the third blue. Which do you choose?\n").lower()
    if stage_3 == "yellow" or stage_3 == "y":
        print("Youi open the door into a grand feast hall. You see familiar faces welcoming you to join them with plates of food and flagons of ale. You win!")
        break
    elif stage_3 == "red" or stage_3 == "r":
        game = False
        print("You open the door and are swarmed by hungry kittens. Game over.")
        break
    elif stage_3 == "blue" or stage_3 == "b":
        game = False
        print("You open the door and find yourself in a timeshare sales event. Game over.")
        break
    else:
        print("Red, Yellow, or Blue?\n")
