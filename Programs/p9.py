# Write a program to remove all the odd numbers from an array.

def remove_odd_numbers(arr):
    # Create a new list with only the even numbers
    even_numbers = [num for num in arr if num % 2 == 0]
    return even_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cleaned_numbers = remove_odd_numbers(numbers)

print("Original array:", numbers)
print("Array without odd numbers:", cleaned_numbers)

