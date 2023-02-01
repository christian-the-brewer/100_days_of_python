#Day 25
# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = [int(day[1]) for day in data if day[1] != "temp"]
#     for temp in temps:
#         print(temp)
    
import pandas as pd

data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()

# average = sum(temp_list) / len(temp_list)
# print(data["temp"].max())

