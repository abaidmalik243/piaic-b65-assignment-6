# Write a program that has an array of numbers; if the number is negative, it should remove the negative number from the array.

def remove_negatives(arr):
    # Create a new list with only non-negative numbers
    positive_numbers = [num for num in arr if num >= 0]
    return positive_numbers

# Example usage
numbers = [10, -5, 3, -8, 0, 7, -1]
cleaned_numbers = remove_negatives(numbers)
print("Original array:", numbers)
print("Array without negative numbers:", cleaned_numbers)


# OutPut example
# Original array: [10, -5, 3, -8, 0, 7, -1]
# Array without negative numbers: [10, 3, 0, 7]

