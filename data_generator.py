import csv
import random


START_DISTANCE_CM = 100
MIN_STEP_CM = 2
MAX_STEP_CM = 8


def generate_sensor_data():
    distance = START_DISTANCE_CM

    with open("sensor_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["distance"])

        while distance > 0:
            distance = max(
                0,
                distance - random.randint(MIN_STEP_CM, MAX_STEP_CM)
            )

            writer.writerow([distance])

    print("Sensor data generated successfully.")


if __name__ == "__main__":
    generate_sensor_data()