# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
OFFSET = 32  # The difference between Fahrenheit and Celsius zero points

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global conversion factor to convert Fahrenheit to Celsius
    celsius = (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global conversion factor to convert Celsius to Fahrenheit
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET
    return fahrenheit

# Function to handle user interaction and temperature conversion
def main():
    # Prompt the user for input
    temp = input("Enter the temperature (numeric value): ").strip()
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    # Input validation for numeric temperature
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Perform the appropriate conversion based on the unit
    if unit == "C":
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif unit == "F":
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Entry point of the script
if __name__ == "__main__":
    main()
