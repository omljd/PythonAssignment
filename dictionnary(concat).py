#Write a Python script to concatenate the following dictionaries to create a new one. 

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Initialize a new dictionary to store the concatenated result
result = {}

# Update the result dictionary with the key-value pairs from dic1
for key in dic1:
    result[key] = dic1[key]

# Update the result dictionary with the key-value pairs from dic2
for key in dic2:
    result[key] = dic2[key]

# Update the result dictionary with the key-value pairs from dic3
for key in dic3:
    result[key] = dic3[key]

# Print the resulting concatenated dictionary
print("The concatenated dictionary is:", result)


#Output:- The concatenated dictionary is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

