# Create a function that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.

def factorial(n):
    # Initialize the result to 1 (factorial of 0 is 1)
    result = 1
    
    # Check if the input is a positive integer
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    # Use a while loop to calculate the factorial
    while n > 0:
        result *= n  # Multiply result by the current value of n
        n -= 1       # Decrement n by 1
        
    return result

# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")
