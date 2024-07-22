# Write a Python program and calculate the mean of the below dictionary.

# Dictionary of test values
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

# Initialize a variable to store the sum of the values
total = 0

# Iterate through each value in the dictionary
for value in test_dict.values():
    # Add the current value to the total
    total += value

# Calculate the mean by dividing the total by the number of items in the dictionary
mean = total / len(test_dict)

# Print the mean
print("The mean of the values in the dictionary is:", mean)


#Output:-The mean of the values in the dictionary is: 6.2
