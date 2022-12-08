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

#Ticket exercise
ticket = 0

print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?: "))
if height >= 120:
    age = int(input("How old are you?: "))
    if age < 12:
        print("Child tickets are $5.")
        ticket += 5
    elif age < 18:
        print("Youth tickets are $7.")
        ticket += 7
    else:
        print("Adult tickets are $12.")
        ticket += 12
    while True:
        photo_choice = input("Would you like a photo for only $3 more? y/n: ")
        if photo_choice == "y":
            ticket += 3
            break
        elif photo_choice == "n":
            break
        else:
            print("Please enter y or n: ")
    print(f"Your total comes to ${ticket}.")
else:
    print("Sorry, but the minimum height to ride is 120cm.")