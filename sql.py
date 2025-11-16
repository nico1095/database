# Program Name: sql.py 
# Course: IT3883/Section W02
# Student Name: Anthony Giso
# Assignment Number: 5
# Due Date: 11/16/ 2025
# Purpose: Python program to create and interact with a database. 
import sqlite3

# ---------- 1. Create SQLite database ----------
conn = sqlite3.connect("temperatures.db")
cursor = conn.cursor()

# ---------- 2. Create table (NO triple quotes) ----------
cursor.execute(
    "CREATE TABLE IF NOT EXISTS TemperatureReadings ("
    "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
    "Day_Of_Week TEXT, "
    "Temperature_Value REAL);"
)

# ---------- 3. Insert data from the input file ----------
with open("Assignment5input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            day = parts[0]
            temp = float(parts[1])
            cursor.execute(
                "INSERT INTO TemperatureReadings (Day_Of_Week, Temperature_Value) "
                "VALUES (?, ?);",
                (day, temp)
            )

conn.commit()

# ---------- 4. Compute averages (NO triple quotes) ----------
cursor.execute(
    "SELECT AVG(Temperature_Value) FROM TemperatureReadings WHERE Day_Of_Week = 'Sunday';"
)
avg_sunday = cursor.fetchone()[0]

cursor.execute(
    "SELECT AVG(Temperature_Value) FROM TemperatureReadings WHERE Day_Of_Week = 'Thursday';"
)
avg_thursday = cursor.fetchone()[0]

# ---------- Print results ----------
print(f"Average Sunday Temperature: {avg_sunday:.2f}")
print(f"Average Thursday Temperature: {avg_thursday:.2f}")

conn.close()
