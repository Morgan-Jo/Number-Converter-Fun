import unittest
import math
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

class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_nth_root(self):
        self.assertEqual(round(nth_root(27, 3), 6), 3.0)
        with self.assertRaises(ValueError):
            nth_root(-8, 2)

    def test_trig_deg(self):
        self.assertAlmostEqual(sin_deg(30), 0.5, places=7)
        self.assertAlmostEqual(cos_deg(60), 0.5, places=7)
        self.assertAlmostEqual(tan_deg(45), 1.0, places=7)

    def test_ln(self):
        self.assertAlmostEqual(ln(math.e), 1.0, places=7)
        with self.assertRaises(ValueError):
            ln(0)

    def test_log10(self):
        self.assertAlmostEqual(log10(100), 2.0, places=7)
        with self.assertRaises(ValueError):
            log10(0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(3.5)

if __name__ == "__main__":
    unittest.main()