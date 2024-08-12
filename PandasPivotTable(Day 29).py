"""Write a Pandas program to create a Pivot table and find the total sale amount
region wise, manager wise, sales man wise.
Input:Download the file salesdata.csv From LMS Output:"""
import pandas as pd

# Load the sales data from the CSV file
file_path = r'C:\Users\omlun\Downloads\salesdata.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to understand its structure
print("DataFrame:")
print(df.head())

# Check and print the column names to verify the correct names
print("\nColumn names in the DataFrame:")
print(df.columns)

# Update this line to use the correct column name found in the print statement above
pivot_table = pd.pivot_table(df, values=['Sale_amt'],  # Update this if necessary
                             index=['Region', 'Manager', 'SalesMan'], 
                             aggfunc='sum')

# Display the Pivot table
print("\nPivot Table:")
print(pivot_table)

"""Output:-

DataFrame:
    Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
0     East   Martha  Alexander    Television     95      1198.0  113810.0
1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
2  Central  Hermann       Luis    Television     36      1198.0   43128.0
3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
4     West  Timothy    Stephen    Television     56      1198.0   67088.0

Column names in the DataFrame:
Index(['Region', 'Manager', 'SalesMan', 'Item', 'Units', 'Unit_price',
       'Sale_amt'],
      dtype='object')

Pivot Table:
                           Sale_amt
Region  Manager SalesMan           
Central Douglas John       124016.0
        Hermann Luis       206373.0
                Shelli      33698.0
                Sigal      125037.5
        Marth   Steven      14000.0
        Martha  Steven     185690.0
        Timothy David      140955.0
East    Douglas Karen       48204.0
        Martha  Alexander  236703.0
                Diana       36100.0
West    Douglas Michael     66836.0
        Timothy Stephen     88063.0
"""
