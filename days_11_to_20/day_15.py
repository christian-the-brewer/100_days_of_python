#Day 15

# Coffee machine simulator

import os
from coffee_art import logo

#coffee machine supplies
supplies = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


#drinks

espresso = {
    "name": "espresso",
    "water": 50,
    "milk": 0,
    "coffee": 18,
    "price": 1.5,
}
latte = {
    "name": "latte",
    "water": 200,
    "milk": 150,
    "coffee": 24,
    "price": 2.5,
}
cappuccino = {
    "name": "cappuccino",
    "water": 250,
    "milk": 100,
    "coffee": 24,
    "price": 3.0,
}

#dict to convert user input to drink
drinks = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
}

#clears screen
def clear():
    os.system("clear")

#check if enough supplies
def check(drink, supplies):
    """takes in a drink and current supplies and returns true or false if there are enough supplies"""
    # print(f"This is drink: {drink}")
    # print(f"This is supplies: {supplies}")
    for supply in supplies:
        # print(supply)
        if supply != "money":
            if drink[supply] > supplies[supply]:
                return False
    return True

# print(check(espresso, supplies))

#print supplies
def print_supplies(supplies):
    """Prints current supplies"""
    water = supplies["water"]
    milk = supplies["milk"]
    coffee = supplies["coffee"]
    money = supplies["money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"
            
# print(print_supplies(supplies))

#fill supplies
def fill(supplies):
    """returns max supplies and current money"""
    print("Supplies refilled.")
    return {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": supplies["money"],
}

# payment
def payment_check(drink):
    """takes a drink and asks for payment. returns true or false."""
    cost = drink["price"]
    bev = drink["name"]
    print(f"Please enter ${cost}.")
    while True:
        quarters = (input("How many quarters?: "))
        if quarters.isdigit():
            if int(quarters) >= 0:
                quarters = int(quarters) * .25
                break
    while True:
        dimes = (input("How many dimes?: "))
        if dimes.isdigit():
            if int(dimes) >= 0:
                dimes = int(dimes) * .1
                break
    while True:
        nickles = (input("How many nickles?: "))
        if nickles.isdigit():
            if int(nickles) >= 0:
                nickles = int(nickles) * .05
                break
    while True:
        pennies = (input("How many pennies?: "))
        if pennies.isdigit():
            if int(pennies) >= 0:
                pennies = int(pennies) * .01
                break
    payment = quarters + dimes + nickles + pennies
    
    if payment >= cost:
        if payment != cost:
            print(f"Here is ${payment - cost} in change.")
        print(f"Here is your {bev}, Enjoy!")
        return True
    else:
        print(f"Insufficent funds. Returning ${payment}")
        return False

# payment_check(latte)

#help
def help():
    """Brings up help menu."""
    print("'report': shows current supplies")
    print("'fill': refills supplies")
    print("'report': shows current supplies")
    print("'espresso': orders an espresso")
    print("'latte': orders an latte")
    print("'cappuccino': orders an cappuccino")
    print("'quit': close program")

clear()
print(logo)
while True:
    user = input("What would you like? (espresso/latte/cappuccino/help): ").lower()
    if user == "report":
        print(print_supplies(supplies))
    elif user == "refill":
        supplies = fill(supplies)
        print(print_supplies(supplies))
    elif user == "espresso" or user == "latte" or user == "cappuccino":
        drink = drinks[user]
        if check(drink, supplies):
            if payment_check(drink):
                supplies["water"] -= drink["water"]
                supplies["milk"] -= drink["milk"]
                supplies["coffee"] -= drink["coffee"]
                supplies["money"] += drink["price"]
        else:
                print("Sorry, not enough supplies for that. Please 'refill'.")
    elif user == "help":
        help()
    elif user == "quit" or user == "q" or user == "end" or user == "close":
        print("Shutting down...")
        break
        
        


    









