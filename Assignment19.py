#Write a Python script to concatenate the following dictionaries to create a new one.

# Define the sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries
#Using the update() method
concatenated_dict = {}
for dic in (dic1, dic2, dic3):
    concatenated_dict.update(dic)

# Print the concatenated dictionary
print("New_Dictionry:-",concatenated_dict)

#Output: New_Dictionry:-{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
