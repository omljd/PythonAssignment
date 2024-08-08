""" Suppose you want to track and analyze your household expenses for a month.
You have recorded the expenses for various categories, such as groceries,tilities,
rent, transportation, and entertainment.You can represent this expense data
using a Pandas Series. """

import pandas as pd

# Input data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# Create the Pandas Series
expenses_series = pd.Series(data=expenses, index=categories)

# Display the Series
print(expenses_series)

# Calculate the total monthly expenses
total_expenses = expenses_series.sum()
print(f"Total monthly expenses: ${total_expenses}")

# Calculate the average expense per category
average_expense = expenses_series.mean()
print(f"Average expense per category: ${average_expense:.2f}")

# Identify the most and least expensive categories
most_expensive = expenses_series.idxmax()
least_expensive = expenses_series.idxmin()
print(f"Most expensive category: {most_expensive}")
print(f"Least expensive category: {least_expensive}")


""" Output:-
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
dtype: int64
Total monthly expenses: $2350
Average expense per category: $470.00
Most expensive category: Rent
Least expensive category: Entertainment"""
