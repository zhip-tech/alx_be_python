# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Use global conversion factor to convert F → C
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Use global conversion factor to convert C → F
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Ask for temperature
    temp_input = input("Enter the temperature to convert: ")

    # Validate numeric input
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Ask for temperature unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        celsius_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius_temp}°C")

    elif unit == "C":
        fahrenheit_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit_temp}°F")

    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
