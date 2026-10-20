"""Week 1 tests. Run: python3 -m unittest tests.test_field -v"""
import random
import unittest

from src.field import P, add, sub, neg, mul, inv, inv_euclid, div


class TestField(unittest.TestCase):
    def test_add_wrap(self):
        self.assertEqual(add(96, 2), 1)

    def test_sub_wraps_below_zero(self):
        self.assertEqual(sub(3, 5), 95)

    def test_neg(self):
        self.assertEqual(neg(1), 96)
        self.assertEqual(neg(0), 0)

    def test_mul_wrap(self):
        self.assertEqual(mul(15, 10), 53)

    def test_inputs_are_normalised(self):
        # negative and oversized inputs must still land in [0, p)
        self.assertEqual(add(-1, 0), 96)
        self.assertEqual(mul(-2, 3), 91)
        self.assertEqual(add(200, 0), 6)

    def test_inverse_every_nonzero_element(self):
        for a in range(1, P):
            self.assertEqual(mul(a, inv(a)), 1, a)

    def test_fermat_and_euclid_agree(self):
        for a in range(1, P):
            self.assertEqual(inv(a), inv_euclid(a), a)

    def test_inverse_other_prime(self):
        p = 2**61 - 1
        a = 123456789
        self.assertEqual(a * inv(a, p) % p, 1)
        self.assertEqual(inv(a, p), inv_euclid(a, p))

    def test_div(self):
        self.assertEqual(div(15, 5), 3)
        self.assertEqual(mul(div(7, 3), 3), 7)

    def test_zero_has_no_inverse(self):
        for f in (inv, inv_euclid):
            with self.assertRaises(ZeroDivisionError):
                f(0)
            with self.assertRaises(ZeroDivisionError):
                f(P)  # P is 0 in the field
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

    def test_field_axioms_random(self):
        rng = random.Random(1)
        for _ in range(200):
            a, b, c = (rng.randrange(P) for _ in range(3))
            self.assertEqual(mul(a, add(b, c)), add(mul(a, b), mul(a, c)))
            self.assertEqual(add(a, neg(a)), 0)


if __name__ == "__main__":
    unittest.main()
