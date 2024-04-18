import unittest
from domain.models import Operands

class TestOperands(unittest.TestCase):
    def test_operands_creation(self):
        # Test to ensure that the operands are correctly set
        op = Operands(1, 2)
        self.assertEqual(op.first_operand, 1)
        self.assertEqual(op.second_operand, 2)

    def test_operands_must_be_integers(self):
        # This test checks that providing non-integers raises a TypeError
        with self.assertRaises(TypeError):
            Operands('one', 'two')

if __name__ == '__main__':
    unittest.main()
