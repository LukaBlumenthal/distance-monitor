import csv
import random
import time

distance = 100

with open("sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["distance"])
    file.flush()

    while distance > 0:
        distance = distance - random.randint(2, 8)

        if distance <= 0:
            distance = 0

        writer.writerow([distance])
        file.flush()