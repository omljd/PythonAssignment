#Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Create an array of 10 zeros
zeros_array = np.zeros(10)

# Create an array of 10 ones
ones_array = np.ones(10)

# Create an array of 10 fives
fives_array = np.full(10, 5)

# Concatenate the arrays to form the final array
final_array = np.concatenate((zeros_array, ones_array, fives_array))

print(final_array)


""" Output:-[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5.
 5. 5. 5. 5. 5. 5.]"""
