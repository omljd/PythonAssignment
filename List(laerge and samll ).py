#Write a Python program to get the largest and smallest number from a list without builtin functions.

# List of numbers
numbers = [34, 2, 78, 45, 21, 90, 12, 67]

# Initialize variables to store the largest and smallest numbers
# Set them to the first element of the list
largest = numbers[0]
smallest = numbers[0]

# Iterate through each number in the list
for number in numbers:
    # Update largest if the current number is greater
    if number > largest:
        largest = number
    # Update smallest if the current number is smaller
    if number < smallest:
        smallest = number

# Print the largest and smallest numbers
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

#Output:-
"""The largest number in the list is: 90
The smallest number in the list is: 2"""

