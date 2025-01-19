class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b



import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various number combinations."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(10, 20), 30)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, -5), -5)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_add_(self):
        """Test addition with positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, -5), -5)

    def test_add(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtraction(5, 3), 2)
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(3, 3), 0)

    def test_subtraction(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtraction(-2, -3), 1)
        self.assertEqual(self.calc.subtraction(-5, 5), -10)
        self.assertEqual(self.calc.subtraction(0, -5), 5)

    def test_subtraction(self):
        """Test subtraction with floating point numbers."""
        self.assertAlmostEqual(self.calc.subtraction(0.3, 0.1), 0.2, places=7)
        self.assertEqual(self.calc.subtraction(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(self.calc.multiplication(2, 3), 6)
        self.assertEqual(self.calc.multiplication(0, 5), 0)
        self.assertEqual(self.calc.multiplication(10, 10), 100)

    def test_multiplication(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiplication(-2, -3), 6)
        self.assertEqual(self.calc.multiplication(-2, 3), -6)
        self.assertEqual(self.calc.multiplication(0, -5), 0)

    def test_multiplication(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(self.calc.multiplication(0.1, 0.2), 0.02, places=7)
        self.assertEqual(self.calc.multiply(2.5, 2.0), 5.0)

    def test_divide(self):
        """Test division with positive numbers."""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.division(-6, -2), 3)
        self.assertEqual(self.calc.division(-6, 2), -3)
        self.assertEqual(self.calc.division(6, -2), -3)

    def test_division(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(self.calc.division(0.3, 0.1), 3.0, places=7)
        self.assertEqual(self.calc.division(5.0, 2.0), 2.5)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.division(5, 0))
        self.assertIsNone(self.calc.division(0, 0))
        self.assertIsNone(self.calc.division(-5, 0))

if __name__ == '__main__':
    unittest.main()
