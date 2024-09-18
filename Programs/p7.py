# Create a function that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.

def sum_of_array(arr):
    total = 0  # Initialize sum to 0
    i = 0  # Initialize index counter
    
    # Use a while loop to iterate through the array
    while i < len(arr):
        total += arr[i]  # Add current element to the total
        i += 1  # Move to the next index
    
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
result = sum_of_array(numbers)
print(f"The sum of the array is: {result}")
