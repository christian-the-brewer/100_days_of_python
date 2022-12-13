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

# #check modulo of every number up to half of the selected number

# def check_prime(number):
#     if number == 1:
#         return False
#     i = 2
#     while i <= number / 2:
#         if number % i == 0:
#             print(i)
#             return False
#         else:
#             print(i)
#             i += 1
#     return True

# print(check_prime(1))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet.extend(alphabet)

while True:
    direction = input("Enter 'encode' to encrypt a message, or decode to decrypt it:\n").lower()
    if direction == "encode":
        message = input("Enter your message to be encrypted:\n").lower()
        break
    elif direction == "decode":
        message = input("Enter your code to be decrypted:\n"). lower()
        break
    else:
        print("Please enter 'encode' or 'decode'")
        
while True:
    shift = int(input("Enter the shift number you would like to use:\n"))
    if isinstance(shift, int) and shift > 0:
        break
    else:
        print("Please enter a positive whole number")

def cypher(text, shift, direction):
    char_list = []

    while shift > 26:
        shift -= 26
        print(f"reducing shift to {shift}")

    for char in text:
        print(direction)
        if direction == "encode":
            x = alphabet.index(char)
            char = alphabet[x + shift]
            char_list.append(char)
        else: 
            x = (alphabet.index(char) + 26)
            char = alphabet[x - shift]
            char_list.append(char)

    return "".join(char_list)


print(cypher(message, shift, direction))
# def encode(string, shift):
#     #handle overly large shift values by reducing them by 26 so they still result in the same shifted value but stay within the bounds of the list.
#     char_list = []

   
#     for char in string:
        
#         x = alphabet.index(char)
#         char = alphabet[x + shift]
#         print(char)
#         char_list.append(char)
#         print(char_list)

#     return "".join(char_list)

# def decode(string, shift):
#     char_list = []

#     while shift > 26:
#         shift -= 26
#         print(f"reducing shift to {shift}")
    
#     for char in string:
        
#         x = (alphabet.index(char) + 26)
#         char = alphabet[x - shift]
#         print(char)
#         char_list.append(char)
#         print(char_list)

#     return "".join(char_list)

    
