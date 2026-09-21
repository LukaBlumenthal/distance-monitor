import csv
import time
from datetime import datetime

with open("sensor_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            distance = int(row["distance"])
        except ValueError:
            print(f"Invalid sensor value: {row['distance']}")
            continue

        if distance < 20:
            status = "STOP"
        elif distance <= 50:
            status = "WARNING"
        else:
            status = "OK"

        print(f"Distance: {distance} cm | Status: {status}")

        if status == "WARNING" or status == "STOP":
            current_time = datetime.now()

            with open("warning_log.txt", "a") as log_file:
                log_file.write(
                    f"{current_time} | Distance: {distance} cm | Status: {status}\n"
                )

        time.sleep(1)