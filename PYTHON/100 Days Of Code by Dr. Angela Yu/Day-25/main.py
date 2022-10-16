# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas


# data = pandas.read_csv("weather_data.csv")
# x = dir(pandas)
# print(x)
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())

# print(data["temp"].max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

# Create Dataframe from scratch
# data_dict = {
#     "students": ["Angela", "James", "Cliffton"],
#     "score": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"]
grey_count = len(colors[colors == "Gray"])
cinnamon_count = len(colors[colors == "Cinnamon"])
black_count = len(colors[colors == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, cinnamon_count, black_count]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")

