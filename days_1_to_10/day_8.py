#Day 8 

# #functions continued
# def greet():
#     print("Hello")
#     print("Hi")
#     print("sup")

# def greet_with(name, location):
#     print(f"Hello {name}, from {location}")

# greet_with("Christian", "Malden")

# greet_with(location="Malden", name="Christian")

# #Coding Challenge Paint can Calculator

# import math 

# def paint_can_calculate(width, height, can):
#     total_area = float(width) * float(height)
#     return math.ceil(total_area / float(can)) 

# print(paint_can_calculate(5.4,6.1,5))

#Prime number checker

#check modulo of every number up to half of the selected number

def check_prime(number):
    if number == 1:
        return False
    i = 2
    while i <= number / 2:
        if number % i == 0:
            print(i)
            return False
        else:
            print(i)
            i += 1
    return True

print(check_prime(1))