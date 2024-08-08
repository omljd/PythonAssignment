"""Write a Pandas program to split the following data frame into groups based
on Class and count the number of students in that particular class.
Also generate a bar chart based on the result and explain the conclusion."""

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the DataFrame with the given student data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],  # School codes
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],  # Class levels
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],  # Student names
    'age': [12, 12, 13, 13, 14, 12],  # Ages of the students
    'height': [173, 192, 186, 167, 151, 159],  # Heights of the students
    'weight': [35, 32, 33, 30, 31, 32],  # Weights of the students
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']  # Addresses of the students
})

# Step 2: Group by 'class' and count the number of students in each class
class_counts = student_data.groupby('class').size()  # Count the number of students in each class

# Step 3: Generate a bar chart based on the result
class_counts.plot(kind='bar', color='skyblue')  # Plot a bar chart with counts
plt.title('Number of Students in Each Class')  # Add a title to the chart
plt.xlabel('Class')  # Label the x-axis
plt.ylabel('Number of Students')  # Label the y-axis
plt.xticks(rotation=0)  # Rotate the x-axis labels for better readability
plt.show()  # Display the bar chart

# Step 4: Output the class counts
print(class_counts)  # Print the counts for each class
