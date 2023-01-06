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
    "water": 50,
    "milk": 0,
    "coffee": 18,
    "price": 1.5,
}
latte = {
    "water": 200,
    "milk": 150,
    "coffee": 24,
    "price": 2.5,
}
cappuccino = {
    "water": 250,
    "milk": 100,
    "coffee": 24,
    "price": 3.0,
}

#check if enough supplies
def check(drink, supplies):
    """takes in a drink and current supplies and returns true or false if there are enough supplies"""
    for supply in supplies:
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


