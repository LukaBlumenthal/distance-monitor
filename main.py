import csv

with open("sensor_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        distance = int(row["distance"])
        print(f"Distance: {distance} cm")