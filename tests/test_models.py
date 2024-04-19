import unittest

from src.pytemplate.domain.models import Operands, operands_factory


class TestOperands(unittest.TestCase):
    def test_operands_creation(self):
        # Test to ensure that the operands are correctly set
        op = Operands(1, 2)
        self.assertEqual(op.first_operand, 1)
        self.assertEqual(op.second_operand, 2)

    def test_operands_must_be_integers(self):
        # This test checks that providing non-integers raises a TypeError
        with self.assertRaises(TypeError):
            Operands("one", "two")


class TestOperandsFactory(unittest.TestCase):
    def test_operands_factory_creation(self):
        # Test creating an Operands object through the factory
        op = operands_factory(1, 2)
        self.assertIsInstance(op, Operands)
        self.assertEqual(op.first_operand, 1)
        self.assertEqual(op.second_operand, 2)

    def test_operands_factory_with_non_integers(self):
        # Test that providing non-integers raises a TypeError
        with self.assertRaises(TypeError):
            operands_factory("one", 2)
        with self.assertRaises(TypeError):
            operands_factory(1, "two")


if __name__ == "__main__":
    unittest.main()
