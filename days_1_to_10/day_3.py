#Day 3

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


#Code exercise Love Calculator

first = input("Love Calculator\nEnter your name: ").lower()
second = input("Enter your partner's name: ").lower()
name = first + second
true_count = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love_count = name.count("l") + name.count("o") + name.count("v") + name.count("e")
score = str(true_count) + str(love_count)
if score == "00":
    print("Your score is 0, you go together like coke and mentos.")
elif int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
