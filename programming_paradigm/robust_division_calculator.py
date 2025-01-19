def safe_divide(numerator, denominator):
    """
    Safely perform division with error handling for zero division and non-numeric inputs.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        str: A message containing either the result or an error description
    """
    try:
        # Convert inputs to float and perform division
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
            
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"



import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
