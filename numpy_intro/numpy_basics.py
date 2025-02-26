 
import numpy as np

# Creating arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Printing the arrays
print("Array 1:", array1)
print("Array 2:", array2)

# Performing arithmetic operations
sum_array = array1 + array2
print("Sum of arrays:", sum_array)

diff_array = array1 - array2
print("Difference of arrays:", diff_array)

prod_array = array1 * array2
print("Product of arrays:", prod_array)

quot_array = array1 / array2
print("Quotient of arrays:", quot_array)

# Using basic NumPy functions
mean_array1 = np.mean(array1)
mean_array2 = np.mean(array2)
print("Mean of Array 1:", mean_array1)
print("Mean of Array 2:", mean_array2)

max_array1 = np.max(array1)
max_array2 = np.max(array2)
print("Max of Array 1:", max_array1)
print("Max of Array 2:", max_array2)

min_array1 = np.min(array1)
min_array2 = np.min(array2)
print("Min of Array 1:", min_array1)
print("Min of Array 2:", min_array2)

# Reshaping an array
reshaped_array = np.reshape(array1, (1, 5))
print("Reshaped Array 1:", reshaped_array)