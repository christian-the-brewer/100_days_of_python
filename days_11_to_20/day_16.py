#day 16

# import turtle
# from prettytable import PrettyTable

# # timmy = turtle.Turtle()
# # timmy.shape("turtle")
# # timmy.color("purple", "yellow")

# # print(timmy)

# # my_screen = turtle.Screen()

# # print(my_screen.canvheight)
# # timmy.fd(100)
# # my_screen.exitonclick()

# my_table = PrettyTable()
# my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# my_table.add_column("Type", ["Electric", "Water", "Fire"])
# my_table.align = "l"
# print(my_table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        
