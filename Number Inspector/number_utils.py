import math

def is_prime(n: int) -> bool:
    """
    Check if an integer n is a prime number.

    Rules:
    - n <= 1: not prime
    - 2 is prime
    - Even numbers > 2: not prime
    - For odd n > 2, check factors from 3 to sqrt(n) in steps of 2.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def get_factors(n: int) -> list[int]:
    """
    Return a sorted list of all positive factors of n.

    - For n == 0, raise a ValueError since 0 has infinitely many divisors.
    - For negative n, factors of abs(n) are returned.
    """
    if n == 0:
        raise ValueError("0 has infinitely many divisors. Factors are not listed for 0.")

    factors = set()
    value = abs(n)
    limit = int(math.isqrt(value))

    for i in range(1, limit + 1):
        if value % i == 0:
            factors.add(i)
            factors.add(value // i)

    return sorted(factors)
