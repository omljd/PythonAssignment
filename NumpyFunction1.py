"""Suppose you have a dataset containing daily temperature readings for
a city, and you want to identify days with extreme temperature conditions.
Find days where the temperature either exceeded 35
degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day)."""

import numpy as np

# Given temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-2.0,4.0,-3.0])

# Identify hot days (temperatures > 35°C) using np.where()
hot_days = np.where(temperatures > 35)[0]
# Identify cold days (temperatures < 5°C) using np.where()
cold_days = np.where(temperatures < 5)[0]

# Display the results
print("Hot Days:")
print("Day\tTemperature(°C)")
for index in hot_days:
    print(f"{index + 1}\t{temperatures[index]}")

print("\nCold Days:")
print("Day\tTemperature(°C)")
for index in cold_days:
    print(f"{index + 1}\t{temperatures[index]}")

""" Output:-
Hot Days:
Day	Temperature(°C)
3	36.8
6	38.7
10	37.2

Cold Days:
Day	Temperature(°C)
11	-2.0
12	4.0
13	-3.0 """
