"""Create a bar chart to represent monthly expenses
in different spending categories and give your conclusion.
 Monthly expenses in dollars (replace with your own data) """

# Importing the matplotlib.pyplot library for plotting
import matplotlib.pyplot as plt  

# Data: categories and their corresponding expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Setting the figure size for the plot
plt.figure(figsize=(10, 6))

# Creating the bar chart
plt.bar(categories, expenses, color='skyblue')

# Adding labels and title to the chart
plt.xlabel('Categories')           # Label for the x-axis
plt.ylabel('Expenses (in dollars)') # Label for the y-axis
plt.title('Monthly Expenses by Category')  # Title of the bar chart

# Displaying the bar chart
plt.show()
