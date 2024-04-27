import unittest

from src.pytemplate.domain.models import Operands
from src.pytemplate.service.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator operations."""

    def setUp(self):
        """Setup the Calculator instance for all tests."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition of two numbers."""
        operands = Operands(45, 35)
        result = self.calc.add(operands)
        self.assertEqual(result, 80)

    def test_subtract(self):
        """Test subtraction of two numbers."""
        operands = Operands(45, 35)
        result = self.calc.subtract(operands)
        self.assertEqual(result, 10)

    def test_multiply(self):
        """Test multiplication of two numbers."""
        operands = Operands(45, 35)
        result = self.calc.multiply(operands)
        self.assertEqual(result, 1575)

    def test_divide(self):
        """Test division of two numbers."""
        operands = Operands(45, 35)
        result = self.calc.divide(operands)
        self.assertAlmostEqual(result, 45 / 35)

    def test_divide_by_zero(self):
        """Test division by zero should raise ValueError."""
        operands = Operands(45, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(operands)


if __name__ == "__main__":
    unittest.main()