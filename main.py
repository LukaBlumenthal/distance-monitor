import csv

with open("sensor_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        distance = int(row["distance"])
        
        if distance < 20:
           status = "STOP"
        elif distance <= 50:
           status = "WARNING"
        else:
           status = "OK"

        print(f"Distance: {distance} cm | Status: {status}")