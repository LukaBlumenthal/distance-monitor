# Distance Monitor

A small Python project for processing simulated distance sensor data.

## V1
- Reads distance values from a CSV file
- Displays the values in the terminal

## V2
- Classifies distance values as OK, WARNING, or STOP

## V3
- Generates simulated distance sensor values automatically
- Simulates a robot moving toward a wall
- Prevents negative distance values by stopping at 0 cm

## V4
- Displays sensor values with a delay to simulate measurements over time

## V5
- Handles invalid sensor values without crashing

## V6
- Logs WARNING and STOP events to a text file
- Adds timestamps to logged events

## How to Run
1. Run `data_generator.py` to generate simulated sensor data.
2. Run `main.py` to process and classify the values.
3. Check `warning_log.txt` for WARNING and STOP events.

## What I Learned
- Reading and writing CSV files in Python
- Using loops and conditions
- Generating random values
- Handling errors with `try` and `except`
- Writing log files
- Working with timestamps
- Using Git to save project versions
