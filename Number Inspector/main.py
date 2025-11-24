import sys
from number_utils import is_prime, get_factors

def handle_number(n: int) -> None:
    """
    Given an integer n, print whether it is prime and its factors.
    """
    print(f"Number: {n}")

    # Prime information
    prime_flag = is_prime(n)
    prime_text = "Yes" if prime_flag else "No"
    print(f"Prime: {prime_text}")

    # Factor information
    try:
        factors = get_factors(n)
        print(f"Factors: {factors}")
    except ValueError as e:
        print(f"Factors: {e}")


def main():
    # Case 1: number provided as a command-line argument
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        try:
            n = int(arg)
        except ValueError:
            print(f"Error: '{arg}' is not a valid integer.")
            sys.exit(1)
        handle_number(n)
        return

    # Case 2: interactive prompt
    user_input = input("Enter an integer: ").strip()
    try:
        n = int(user_input)
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer.")
        sys.exit(1)

    handle_number(n)


if __name__ == "__main__":
    main()
