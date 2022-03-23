# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
# for i in range(len(data)):
#     data[i] = data[i].strip()
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     # for row in data:
#     #     print(row)
#     temperatures = []
#     first_line = True
#     for row in data:
#         if not first_line:
#             temperatures.append(int(row[1]))
#         first_line = False
#     print(temperatures)


# import pandas
