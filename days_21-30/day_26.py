# Day 26
# List comprhension

# numbers = [1,2,3]

# new_list = [number*2 for number in numbers]
# print(new_list)

# a_list = [number * 2 for number in range(1,5)]
# print(a_list)
# names = ["Beth", "Dave", "Matt"]
# upper = [name.upper() for name in names]
# print(upper)

# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared = [number ** 2 for number in numbers]
# print(squared)
# evens = [number for number in numbers if number % 2 == 0]
# print(evens)
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()

# with open("file2.txt") as file2:
#     file2_data = file2.readlines()

# result = [int(number) for number in file1_data if number in file2_data]

# print(result)

# dictionary comprehension
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

# passed_students = {student:"passed" for (student, score) in student_scores.items() if score > 59}
# print(passed_students)

# sentence = "What is the airspeed velocity of an unladen swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# weather_f = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}
# print(weather_f)

import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# # for (key, value) in student_dict.items():
# #     print(value)

# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)

# # for (key, value) in student_data_frame.items():
# #     print(value)

# for (index, row) in student_data_frame.iterrows():
#     print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_conversion_dict = {row.letter: row.code for (
    index, row) in data.iterrows()}
print(nato_conversion_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter word: ").upper()
codes = [nato_conversion_dict[letter] for letter in word]
print(codes)
