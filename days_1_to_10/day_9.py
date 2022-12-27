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

#Silent Auction

bids = {}
bidding_finished = False

def find_highest_bid(bidding_record):
    high_bid = 0
    for bidder in bidding_record:
        bid = bidding_record[bidder]
        if bid > high_bid:
            high_bid = bid
            winner = bidder
    return winner

while not bidding_finished:
    name = input("Pleae enter your name: ")
    price = input("Please enter your bid: $")
    bids[name] = price
    while True:
        another_bidder = input("Are there other bidders after you? y/n: ").lower()
        if another_bidder == 'n':
            bidding_finished = True
        elif another_bidder == 'y':



