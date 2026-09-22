import csv
import time
from datetime import datetime


STOP_DISTANCE_CM = 20
WARNING_DISTANCE_CM = 50
MEASUREMENT_DELAY_SECONDS = 1


def classify_distance(distance):
    if distance < STOP_DISTANCE_CM:
        return "STOP"
    elif distance <= WARNING_DISTANCE_CM:
        return "WARNING"
    else:
        return "OK"


def log_event(distance, status):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("warning_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(
            f"{current_time} | Distance: {distance} cm | Status: {status}\n"
        )


def process_sensor_data():
    with open("sensor_data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                distance = int(row["distance"])
            except (ValueError, KeyError):
                print(f"Invalid sensor value: {row.get('distance', 'missing')}")
                continue

            status = classify_distance(distance)

            print(f"Distance: {distance} cm | Status: {status}")

            if status != "OK":
                log_event(distance, status)

            time.sleep(MEASUREMENT_DELAY_SECONDS)


if __name__ == "__main__":
    process_sensor_data()