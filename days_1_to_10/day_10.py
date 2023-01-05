#Day 10

# def format_name(f_name, l_name):
#     """"An example of a function that titles a first and last name"""
#     if f_name == "" or l_name == "":
#         return print("invalid inputs")

#     return f"{f_name.title()} {l_name.title()}"

# print(format_name( "", "brewer"))

# format_name()

#Calculator Challenge
#functions for calculating

from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    num1 = int(input("Enter first number: "))

    for key in operations:
        print(key)

    should_continue = True

    while should_continue:

        operation_sign = input("Press operation: ")

        num2 = float(input("Enter next number: "))

        calculate = operations[operation_sign]
        answer = calculate(num1, num2)
        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' y to continue with {answer}, or 'n' to start over: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


