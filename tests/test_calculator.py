import unittest
from functions import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, '+', 2), 4)

    def test_subtraction(self):
        self.assertEqual(calculate(5, '-', 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculate(3, '*', 3), 9)

    def test_division(self):
        self.assertEqual(calculate(10, '/', 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, '/', 0)

    def test_sqrt(self):
        self.assertEqual(calculate(9, '√'), 3)

    def test_power(self):
        self.assertEqual(calculate(2, '^', 3), 8)

if __name__ == "__main__":
    unittest.main()
