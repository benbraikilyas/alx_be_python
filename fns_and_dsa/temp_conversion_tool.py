#!/usr/bin/env python3

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius using global conversion factor."""
    try:
        fahrenheit = float(fahrenheit)
        return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit using global conversion factor."""
    try:
        celsius = float(celsius)
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    while True:
        try:
            # Get temperature input
            temp = input("\nEnter the temperature to convert (or 'q' to quit): ")
            if temp.lower() == 'q':
                print("Goodbye!")
                break

            # Get unit input
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            
            # Perform conversion based on input unit
            if unit == 'C':
                result = convert_to_fahrenheit(temp)
                print(f"{float(temp):.1f}°C is {result:.1f}°F")
            elif unit == 'F':
                result = convert_to_celsius(temp)
                print(f"{float(temp):.1f}°F is {result:.1f}°C")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                
        except ValueError as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
