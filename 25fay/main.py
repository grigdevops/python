# import csv
# import pandas

# data = []

# with open("weather_data.csv") as weather_file:
#     weather = weather_file.readlines()
#
# print(weather)

# with open("weather_data.csv") as weather_file:
#     weather = csv.reader(weather_file)
#     temperatures = []
#     for row in weather:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # for i in range(1,8):
#         #     print(i)
# print(temperatures)


# data =pandas.read_csv("weather_data.csv")
# # print(weather)
# # print(type(data))
# # print(type(data["temp"]))
#
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# data_temp_list = data["temp"].to_list()
# print(data_temp_list)

# def Average(lst):
#     return sum(lst) / len(lst)
#
# average = Average(data_temp_list)
# # print(average)

#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
#
# print(data.condition)

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
# print(data.temp.max())

# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# data_dict = {
#     "students": ["Amy", "John", "Angela"] ,
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("count.csv")




