# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature_input():
    """
    Prompts the user for temperature input and ensures it is a numeric value.
    """
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            if temp_input.lower() == 'exit':
                return None
            temperature = float(temp_input)
            return temperature
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def main():
    """
    Main function to interact with the user for temperature conversion.
    """
    while True:
        temperature = get_temperature_input()
        if temperature is None:
            print("Exiting the program. Goodbye!")
            break

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C.")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
