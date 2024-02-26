import numpy as np

# Example 3x3 array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# List of values to check against
values_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Flatten the array into a single list
flattened_array = array.flatten()

# Check if all elements of the flattened array are in the list of values
result = all(element in values_to_check for element in flattened_array)

# Print the result
print(result)  # Output will be True
