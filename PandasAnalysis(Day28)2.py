"""Write a Pandas program to split the following dataframe by school code and
get mean, min, and max value of age for each school. Also generate a
horizontal bar chart based on the result and explain the conclusion."""

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the DataFrame with the given student data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],  # School codes
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],  # Class levels
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],  # Student names
    'age': [12, 12, 13, 13, 14, 12],  # Ages of the students
    'height': [173, 192, 186, 167, 151, 159],  # Heights of the students
    'weight': [35, 32, 33, 30, 31, 32],  # Weights of the students
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']  # Addresses of the students
})

# Step 2: Group the data by 'school_code' and calculate mean, min, and max of 'age'
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])  
# The 'agg' function is used to apply multiple aggregation functions (mean, min, max) to the 'age' column for each school

# Step 3: Generate a horizontal bar chart based on the result
age_stats.plot(kind='barh', figsize=(8, 6), color=['skyblue', 'lightgreen', 'salmon'])  
# Plot the age statistics using a horizontal bar chart, with custom colors for clarity

plt.title('Age Statistics by School Code')  # Add a title to the chart
plt.xlabel('Age')  # Label the x-axis
plt.ylabel('School Code')  # Label the y-axis
plt.show()  # Display the bar chart

# Step 4: Output the age statistics
print(age_stats)  # Print the calculated mean, min, and max age for each school
