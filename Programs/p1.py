# Create a function that takes an array, an index, and a value as parameters. Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array.

def insert_at_index(arr, index, value):
    arr.insert(index, value)  # Insert the value at the specified index
    return arr  # Return the modified array

# Example usage
my_array = [1, 2, 3, 4]
result = insert_at_index(my_array, 2, 'newValue')
print(result)  # Output: [1, 2, 'newValue', 3, 4]


