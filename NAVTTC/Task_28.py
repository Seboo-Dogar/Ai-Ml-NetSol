# NumPy Creating Arrays

# Create a NumPy ndarray Object
import numpy as np

# Create a 1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1-D Array:")
print(arr1)

# Create a 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D Array:")
print(arr2)

# Create a 3-D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3-D Array:")
print(arr3)

# Create an array of zeros
zeros_array = np.zeros((3, 4))
print("\nArray of Zeros:")
print(zeros_array)

# Create an array of ones
ones_array = np.ones((2, 3))
print("\nArray of Ones:")
print(ones_array)

# Create an array of a specific value
full_array = np.full((2, 2), 7)
print("\nArray of Specific Value:")
print(full_array)


# Check Number of Dimensions
print("\nNumber of Dimensions in arr1:", arr1.ndim)
print("Number of Dimensions in arr2:", arr2.ndim)
print("Number of Dimensions in arr3:", arr3.ndim)