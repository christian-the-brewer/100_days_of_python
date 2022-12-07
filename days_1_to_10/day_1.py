# Day 1

# #Print Exercise
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

#input information from user with input("prompt goes here")

# #Exercise to print length of user inputed name
# print(len(input("What is your name?")))

# #VARIABLES
# name = "Jack"
# print(name)

# name = "Angela" #name variable is reassigned 
# print(name)

# name = input("What is your name?") #storing user input as variable
# length = len(name) #variable storing length of variable name
# print(length)

# #Switch variable data exercise
# a = input("Enter number for a:")
# b = input("Enter number for b:")

# c = a
# a = b
# b = c

# print(f"a: {a}")
# print(f"b: {b}")

#Band name generator
#1. Create a greeting for your program.
print("Welcome to the band name generator.")
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What is your pet\'s name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band's name could be " + city + " " + pet + ".\n" )
#5. Make sure the input cursor shows on a new line:
