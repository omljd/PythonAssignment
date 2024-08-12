"""Write a Pandas program to create a Pivot table and find the item wise unit
sold.
Input:Download the file salesdata.csv From LMS"""
import pandas as pd


# Load the sales data from the CSV file
file_path = r'C:\Users\omlun\Downloads\salesdata.csv'  # Update with the correct path to your CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print("DataFrame:")
print(df.head())

# Create a Pivot table to find the item-wise units sold
pivot_table = pd.pivot_table(df, values='Units',  # Use the correct column name
                             index=['Item'], 
                             aggfunc='sum')

# Display the Pivot table
print("\nPivot Table (Item-wise Units Sold):")
print(pivot_table)

"""Output:-
DataFrame:
    Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
0     East   Martha  Alexander    Television     95      1198.0  113810.0
1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
2  Central  Hermann       Luis    Television     36      1198.0   43128.0
3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
4     West  Timothy    Stephen    Television     56      1198.0   67088.0

Pivot Table (Item-wise Units Sold):
              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
"""
