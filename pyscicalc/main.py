"""Main module for PySciCalc - A simple scientific calculator.""" 

from operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    sqrt,
    nth_root,
    sin_deg,
    cos_deg,
    tan_deg,
    ln,
    log10,
    factorial,
)

def get_float(prompt: str) -> float:
    """Prompt the user for a float and repeat until valid."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int(prompt: str) -> int:
    """Prompt the user for an integer and repeat until valid."""
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def show_menu() -> None:
    print("\n=== PySciCalc ===")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Power")
    print("6) Square root")
    print("7) Nth root")
    print("8) Sine (degrees)")
    print("9) Cosine (degrees)")
    print("10) Tangent (degrees)")
    print("11) Natural log (ln)")
    print("12) Log base 10")
    print("13) Factorial")
    print("0) Exit")

def main() -> None:
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "0":
            print("Goodbye.")
            break

        try:
            if choice == "1":
                a = get_float("Enter first number: ")
                b = get_float("Enter second number: ")
                result = add(a, b)
            elif choice == "2":
                a = get_float("Enter first number: ")
                b = get_float("Enter second number: ")
                result = subtract(a, b)
            elif choice == "3":
                a = get_float("Enter first number: ")
                b = get_float("Enter second number: ")
                result = multiply(a, b)
            elif choice == "4":
                a = get_float("Enter numerator: ")
                b = get_float("Enter denominator: ")
                result = divide(a, b)
            elif choice == "5":
                a = get_float("Enter base: ")
                b = get_float("Enter exponent: ")
                result = power(a, b)
            elif choice == "6":
                x = get_float("Enter number: ")
                result = sqrt(x)
            elif choice == "7":
                x = get_float("Enter number: ")
                n = get_float("Enter root degree: ")
                result = nth_root(x, n)
            elif choice == "8":
                x = get_float("Enter angle in degrees: ")
                result = sin_deg(x)
            elif choice == "9":
                x = get_float("Enter angle in degrees: ")
                result = cos_deg(x)
            elif choice == "10":
                x = get_float("Enter angle in degrees: ")
                result = tan_deg(x)
            elif choice == "11":
                x = get_float("Enter positive number: ")
                result = ln(x)
            elif choice == "12":
                x = get_float("Enter positive number: ")
                result = log10(x)
            elif choice == "13":
                n = get_int("Enter non negative integer: ")
                result = factorial(n)
            else:
                print("Unknown option. Please choose a valid menu item.")
                continue

            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()