# Implement a program that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []  # Array to store converted temperatures
    i = 0  # Initialize index counter

    # Use a while loop to convert each temperature
    while i < len(celsius_list):
        fahrenheit = (celsius_list[i] * 9/5) + 32  # Conversion formula
        fahrenheit_list.append(fahrenheit)  # Add converted temperature to the array
        i += 1  # Move to the next temperature
    
    return fahrenheit_list

# Input from the user
celsius_list = list(map(float, input("Enter temperatures in Celsius (separated by spaces): ").split()))

# Convert temperatures to Fahrenheit
converted_temperatures = celsius_to_fahrenheit(celsius_list)

# Display the converted temperatures
print("Temperatures in Fahrenheit:", converted_temperatures)


