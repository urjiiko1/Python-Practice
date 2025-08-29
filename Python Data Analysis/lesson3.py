import csv
with open("Python Data Analysis\\passengers.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)