#Day 9
# #Coding Challenge

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# #Empty dictionary called student_grades
# student_grades = {}

# for student in student_scores:
    
#     grade = ""
#     if student_scores[student] > 90:
#         grade = "Oustanding"
#     elif student_scores[student] > 80:
#         grade = "Exceeds Expectations"
#     elif student_scores[student] > 70:
#         grade = "Acceptable"
#     else:
#         grade = "Fail"
#     student_grades[student] = grade

# print(student_grades)

# #Nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# #Nesting list inside dictionary
# travel_log = {
#     "France": [
#         "Paris",
#         "Lille",
#         "Dijon"
#     ],
#     "Germany": [
#         "Berlin",
#         "Hamburg",
#         "Stuttgart"
#     ],
# }

# #Nesting list inside dictionary inside dictionary inside dictionary
# travel_log = {
#     "France": {"cities_visited": [
#         "Paris",
#         "Lille",
#         "Dijon"
#         ],
#         "total_visits": 12,
#     },
#     "Germany": {"cities_visited": [
#         "Berlin",
#         "Hamburg",
#         "Stuttgart"
#     ]},
# }

# #Nesting dicts in lists

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# ]

#Coding Challenge
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Function add_new_country
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)