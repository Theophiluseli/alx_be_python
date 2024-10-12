# main.py

import sys
from robust_division_calculator import safe_divide # type: ignore

def main():
    # Ensure two additional arguments (numerator and denominator) are passed
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get the arguments (numerator and denominator)
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
