# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Jessica Scales
# Assignment Number: Lab5
# Due Date: 11/16/2025
# Purpose: This program reads temperature data from an input file,
# inserts the data into a SQLite database, and calculates
# the average temperature for Sunday and Thursday.
# Resources Used:
# Lecture notes
# Python SQLite documentation

import sqlite3

def main():
    # Create / connect to the SQLite database
    conn = sqlite3.connect("temperatures.db")
    cursor = conn.cursor()

    # Create the table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Temperatures (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_Of_Week TEXT,
            Temperature_Value REAL
        )
    """)

    conn.commit()

    # Read the input file and insert data
    try:
        with open(r"C:\Users\msjes\Downloads\Assignment5input.txt", "r") as file:
            for line in file:
                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                # Each line has: Day Temperature
                # Example: "Sunday 46.5"
                parts = line.split()

                # The day is at index 0, temperature at index 1
                day = parts[0]
                temperature = float(parts[1])

                cursor.execute("""
                    INSERT INTO Temperatures (Day_Of_Week, Temperature_Value)
                    VALUES (?, ?)
                """, (day, temperature))

        conn.commit()

    except FileNotFoundError:
        print("Error: Assignment5input.txt was not found.")
        conn.close()
        return

    # Calculate averages
    cursor.execute("""
        SELECT AVG(Temperature_Value)
        FROM Temperatures
        WHERE Day_Of_Week = 'Sunday'
    """)
    sunday_avg = cursor.fetchone()[0]

    cursor.execute("""
        SELECT AVG(Temperature_Value)
        FROM Temperatures
        WHERE Day_Of_Week = 'Thursday'
    """)
    thursday_avg = cursor.fetchone()[0]

    # Print results
    print("Average temperature for Sunday:", round(sunday_avg, 2))
    print("Average temperature for Thursday:", round(thursday_avg, 2))

    # Close database connection
    conn.close()

# Run the program
main()
