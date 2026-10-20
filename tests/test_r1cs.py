"""Week 5 tests. Run: python3 -m unittest tests.test_r1cs -v

Program: out = x^3 + x + 5. Witness layout is fixed: w = [1, out, x, v1] with v1 = x*x.
"""
import unittest

from src.r1cs import P, is_satisfied, cubic_r1cs, cubic_witness


class TestR1CS(unittest.TestCase):
    def setUp(self):
        self.L, self.R, self.O = cubic_r1cs()

    def test_shape(self):
        self.assertEqual(len(self.L), 2)
        for M in (self.L, self.R, self.O):
            for row in M:
                self.assertEqual(len(row), 4)

    def test_witness_layout(self):
        self.assertEqual(cubic_witness(3), [1, 35, 3, 9])

    def test_valid_witnesses(self):
        for x in [0, 1, 2, 3, 50, 96, -4]:
            w = cubic_witness(x)
            self.assertTrue(is_satisfied(self.L, self.R, self.O, w), x)

    def test_wrong_output_rejected(self):
        w = cubic_witness(3)
        w[1] = (w[1] + 1) % P
        self.assertFalse(is_satisfied(self.L, self.R, self.O, w))

    def test_wrong_intermediate_rejected(self):
        w = cubic_witness(3)
        w[3] = (w[3] + 1) % P
        self.assertFalse(is_satisfied(self.L, self.R, self.O, w))

    def test_constant_slot_must_be_one(self):
        w = cubic_witness(3)
        w[0] = 2
        self.assertFalse(is_satisfied(self.L, self.R, self.O, w))

    def test_dimension_mismatch(self):
        with self.assertRaises(ValueError):
            is_satisfied(self.L, self.R, self.O, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
