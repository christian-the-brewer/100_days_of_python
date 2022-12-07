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

# # Coding exercise BMI calculator
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))
# # bmi = str(weight / (height ** 2))
# print(f"Your BMI is {str(int(weight / (height ** 2)))}")

# #rounding
# print(round(8/3, 2)) #rounds 2.66666 down to 2 decimal places

# print(8 // 3) #floor division turns result into int

#coding exercise - Your life in weeks
# calculate how many days, weeks, and months left until you reach 90

# #1 year = 365 days = 52 weeks = 12 months
# while True:
#     age = float(input("What is your age?: "))
#     if 0 < age < 90:
#         break
#     else:
#         print("Please enter an age between 1 and 90 years old")
# years_left = 90 - age
# print(f"You have {years_left * 365} days, {years_left * 52} weeks, and {years_left * 12} months left.")

#Code exercise Tip Calculator
print("Welcome to the tip calculator!")
total = float(input("What was the bill total?: "))
percentage = (float(input("What percentage would you like to tip?: ")) / 100 + 1)
people = int(input("how many people will split the bill?: "))
share = (total * percentage) / people
print(f"Each person should pay: {share}")

