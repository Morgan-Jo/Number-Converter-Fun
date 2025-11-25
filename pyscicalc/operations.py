import math
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """Return the quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a: Number, b: Number) -> Number:
    """Return a raised to the power of b."""
    return a**b

def sqrt(x: Number) -> Number:
    """Return the square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)

def nth_root(x: Number, n: Number) -> Number:
    """Return the n-th root of x.

    Raises:
        ValueError: If n is zero or an even root of a negative number is requested.
    """
    if n == 0:
        raise ValueError("Root degree must not be zero.")
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot take an even root of a negative number.")
    return x ** (1 / n)

def sin_deg(x: Number) -> float:
    """Return sine of x degrees."""
    return math.sin(math.radians(x))

def cos_deg(x: Number) -> float:
    """Return cosine of x degrees."""
    return math.cos(math.radians(x))

def tan_deg(x: Number) -> float:
    """Return tangent of x degrees."""
    return math.tan(math.radians(x))

def ln(x: Number) -> float:
    """Return the natural logarithm of x.

    Raises:
        ValueError: If x is not positive.
    """
    if x <= 0:
        raise ValueError("Natural log is only defined for positive numbers.")
    return math.log(x)

def log10(x: Number) -> float:
    """Return the base 10 logarithm of x.

    Raises:
        ValueError: If x is not positive.
    """
    if x <= 0:
        raise ValueError("Log base 10 is only defined for positive numbers.")
    return math.log10(x)

def factorial(n: int) -> int:
    """Return factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is only defined for non negative integers.")
    return math.factorial(n)