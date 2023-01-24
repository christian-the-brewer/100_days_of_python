#Day 25
# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = [int(day[1]) for day in data if day[1] != "temp"]
#     for temp in temps:
#         print(temp)
    
import pandas as pd

data = pd.Series([1,2,3])
print(data)