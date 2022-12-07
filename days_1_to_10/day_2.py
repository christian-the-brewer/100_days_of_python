# Day 2 

# #String
# print("Hello"[-1]) 

# #ints
# one_million = 100_000_000 #underscores instead of commas
# print(one_million)

# #floats
# a_float = 3.14

# #booleans
# True
# False

# #parsing int result of len to a string to print 
# num_char = str(len(input("What is your name?\n")))
# print(f"Your name has {num_char} characters.")

# type(num_char) #tells you the type of entered value

# print(70 + float("100.5"))

# #coding exercise
# #write program that adds the digits in a 2 digit number
# two_digit_number = str(input("Type a two digit number: "))
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# print(f"{first_digit} + {second_digit} = {first_digit + second_digit}")

# Coding exercise BMI calculator
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
# bmi = str(weight / (height ** 2))
print(f"Your BMI is {str(int(weight / (height ** 2)))}")
