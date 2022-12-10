#Day 5

# #For loops

# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit * 2)

# #Code Challenge Average Height without len or sum
# height_total = 0
# students = 0
# student_heights = input("Enter a list of heights seperated by a single space: ").split()
# for height in student_heights:
#     height = int(height)
#     height_total += height
#     students += 1
# average_height = round(height_total / students)
# print(f"The average height is {average_height}")

# #Code Challenge Highest Score without max/min
# highest_score = 0
# scores = input("Enter scores seperated by a single space: ").split()
# for score in scores:
#     score = int(score)
#     if score > highest_score:
#         highest_score = score
# print(f"Highest score: {highest_score}")

# #range
# for number in range(1,11,2):
#     print(number)

# sum = 0
# for number in range(1,101):
#     sum += number
# print(sum)

# #Coding Challenge Calculating Evens
# sum = 0
# for number in range(1,101):
#     if number % 2 == 0:
#         sum += number
# print(sum)

# #Coding Challenge FizzBuzz
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


#Password Generator Project
import random
#list of available characters of each type
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#ask user how many of each type they want
print("Password Generator")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

number_of_letters = int(nr_letters)
number_of_symbols = int(nr_symbols)
number_of_numbers = int(nr_numbers)

ordered_passcode = []
random_passcode = []

passcode = ""

#randomly pull from the list using a for loop with number as the range // or with a while loop and a count
if number_of_letters > 0:
    for number in range(1,(number_of_letters + 1)):
        selected_letter = letters[random.randint(0,len(letters)-1)]
        ordered_passcode.append(selected_letter)
        
if number_of_symbols > 0:
    for number in range(1,(number_of_symbols + 1)):
        selected_symbol = symbols[random.randint(0,len(symbols)-1)]
        ordered_passcode.append(selected_symbol)
        
if number_of_numbers > 0:
    for number in range(1,(number_of_numbers + 1)):
        selected_number = numbers[random.randint(0,len(numbers) - 1)]
        ordered_passcode.append(selected_number)
        
print(ordered_passcode)

#append them to a new list, and randomly select from this list using the len as a range, 
while len(ordered_passcode) > 0:
    random_number = random.randint(0, len(ordered_passcode) -1 )
    random_passcode.append(ordered_passcode.pop(random_number))

#for loop to construct string from list
for char in random_passcode:
    passcode += char

#randomized password string
print(passcode)     




