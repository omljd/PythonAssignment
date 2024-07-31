""" Calculate the profit made by a company

 Input: revenue = np.array([10000, 12000, 11000, 10500]) 

expenses = np.array([4000, 5000, 4500, 4800])

 Output: Profit: [6000 7000 6500 5700]"""

import numpy as np

# Define the revenue and expenses arrays
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate the profit
profit = revenue - expenses

# Print the profit
print("Profit:", profit)

#Output :- Profit: [6000 7000 6500 5700]
