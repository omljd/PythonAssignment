#Compute the standard deviation of the NumPy array

# Import the NumPy library
import numpy as np  

# Define the NumPy array
arr = np.array([20, 2, 7, 1, 34])

print("arr : ",arr) 
# Print the standard deviation value
print("The standard deviation of the array is:", np.std(arr))


print("\n More percision with float32")
print("std of arr : ",np.std(arr,dtype=np.float32))

print("\n More percision with float64")
print("std of arr : ",np.std(arr,dtype=np.float64))


"""
arr :  [20  2  7  1 34]
The standard deviation of the array is: 12.576167937809991

 More percision with float32
std of arr :  12.576168

 More percision with float64
std of arr :  12.576167937809991
"""
