import pandas
raw_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = raw_data["Primary Fur Color"]
print(color.value_counts())



























"""import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for rows in data:
        if rows[1] != "temp":
            temperatures.append(int(rows[1]))
    print(temperatures)

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
prom = 0
for n in temp_list:
    prom += n
prom = prom / len(temp_list)
print(prom)
print(max(temp_list))
print(data[data.temp == data.temp.max()])"""