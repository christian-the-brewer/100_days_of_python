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

# bids = {}
# bidding_finished = False

# def find_highest_bid(bidding_record):
#     high_bid = 0
#     for bidder in bidding_record:
#         bid = bidding_record[bidder]
#         if bid > high_bid:
#             high_bid = bid
#             winner = bidder
#     return winner

# while not bidding_finished:
#     name = input("Pleae enter your name: ")
#     price = int(input("Please enter your bid: $"))
#     bids[name] = price
#     while True:
#         another_bidder = input("Are there other bidders after you? y/n: ").lower()
#         if another_bidder == 'n':
#             bidding_finished = True
#             find_highest_bid(bids)
#         elif another_bidder == 'y':
#             pass
#         else:
#             print("Please enter y or n: ")

#variables
bids = {} #empty dict to hold names and their bids
bidding_finished = False #bool to determine when to end the bidding while loop

#function find_highest_bidder to determine who won 
def find_highest_bidder(bidding_record): #takes the bids dict as the bidding record
    high_bid = 0 #holds the highest bid as function compares each bid to the next one
    winner = "" #holds name of current highest bidder

    for bidder in bidding_record: #for loop to loop through bidding_record names
        bid = bidding_record[bidder] #variable holds the bidder's bid amount
        if bid > high_bid:
            high_bid = bid #the bid becomes the new high_bid
            winner = bidder #also hold the name of bidder
    return winner

print("Welcome to Marina's Auctions.\nToday you are bidding on a piece of paper I chewed and dropped on the floor.")

while not bidding_finished:
    name = input("Please enter your name: ") #takes bidder's name
    price = int(input("Please enter your bid: $")) #takes user's bid amount
    bids[name] = price #adds dict entry for bidder and their bid

    #asks user if there are following bidders
    bidding_continues = input("Are there other bidders after you? y/n: ").lower()
    if bidding_continues == "n":
        bidding_finished = True
        winner = find_highest_bidder(bids)
        print(f"The winner is {winner} with a bid of {bids[winner]}")
    elif bidding_continues == "y":
        bidding_finished = False
    else: 
        print("Please enter y/n: ")


    



