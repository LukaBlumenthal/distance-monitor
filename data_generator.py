import csv
import random

distance = 100

with open("sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["distance"])

    for _ in range(20):
        distance = distance - random.randint(2, 8)

        if distance <= 0:
            distance = 0
            writer.writerow([distance])
            break

        writer.writerow([distance])