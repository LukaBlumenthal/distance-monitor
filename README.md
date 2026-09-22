# Distance Monitor

A small Python project that simulates a distance monitoring system for a mobile robot.

The project generates simulated distance sensor values as a robot approaches an obstacle. The sensor values are processed and classified into three safety states:

* **OK** – distance greater than 50 cm
* **WARNING** – distance between 20 cm and 50 cm
* **STOP** – distance below 20 cm

WARNING and STOP events are stored in a log file with timestamps.

## Project Structure

`data_generator.py`
Generates simulated distance sensor values and stores them in a CSV file.

`main.py`
Reads the sensor data, validates the values, classifies the distance and logs critical events.

`sensor_data.csv`
Contains the generated sensor measurements.

`warning_log.txt`
Stores WARNING and STOP events with timestamps.

## How to Run

1. Run `data_generator.py` to generate simulated sensor data.
2. Run `main.py` to process the sensor values.
3. Check `warning_log.txt` for recorded WARNING and STOP events.

## Example Output

```text
Distance: 65 cm | Status: OK
Distance: 42 cm | Status: WARNING
Distance: 24 cm | Status: WARNING
Distance: 16 cm | Status: STOP
Distance: 6 cm | Status: STOP
Distance: 0 cm | Status: STOP
```
## Screenshot

![Distance Monitor terminal output](images/terminal_output.png)

Invalid sensor values are ignored without stopping the program.

```text
Invalid sensor value: 5t
```

## Development Progress

The project was developed incrementally through several learning stages.

### V1

* Read distance values from a CSV file
* Display values in the terminal

### V2

* Classify distances as OK, WARNING or STOP

### V3

* Generate simulated distance sensor values automatically
* Simulate a robot moving toward an obstacle
* Prevent negative distance values

### V4

* Add delays to simulate measurements over time

### V5

* Handle invalid sensor values without crashing

### V6

* Log WARNING and STOP events
* Add timestamps to logged events

### V7

* Refactored the program into functions
* Added constants for configurable thresholds
* Improved code readability and structure

## What I Learned

* Reading and writing CSV files with Python
* Working with loops and conditions
* Structuring code using functions
* Generating simulated sensor values
* Handling errors with `try` and `except`
* Writing log files
* Working with timestamps
* Using Git and GitHub for version control

## Future Improvements

Possible future extensions include:

* Replacing simulated data with a real distance sensor
* Visualizing distance measurements
* Adding automated tests
* Connecting the system to a robotics framework such as ROS 2

