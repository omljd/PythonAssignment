"""Visualize the daily temperature changes
over time in a city and give your conclusion
 Monthly expenses in dollars (replace with your own data) 
"""
# Importing the matplotlib.pyplot library for plotting
import matplotlib.pyplot as plt 

# Data: days of the month and their corresponding daily temperatures
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Setting the figure size for the plot
plt.figure(figsize=(12, 6))

# Creating the line chart with markers for each data point
plt.plot(days, temperature, marker='o', linestyle='-', color='b')

# Adding labels and title to the chart
plt.xlabel('Days')               # Label for the x-axis
plt.ylabel('Temperature (°F)')   # Label for the y-axis
plt.title('Daily Temperature Changes Over Time')  # Title of the line chart

# Adding a grid for better readability
plt.grid(True)

# Displaying the line chart
plt.show()
