"""Week 2 tests. Run: python3 -m unittest tests.test_algebra -v"""
import unittest

from src.algebra import is_group, order_of, is_generator, subgroup


class TestAlgebra(unittest.TestCase):
    def test_additive_group_mod_n(self):
        n = 7
        self.assertTrue(is_group(range(n), lambda a, b: (a + b) % n, 0))

    def test_multiplicative_group_mod_p(self):
        p = 11
        self.assertTrue(is_group(range(1, p), lambda a, b: a * b % p, 1))

    def test_zero_breaks_multiplicative_group(self):
        p = 11
        self.assertFalse(is_group(range(p), lambda a, b: a * b % p, 1))

    def test_not_closed(self):
        # {0,1,2} under ordinary addition is not closed
        self.assertFalse(is_group([0, 1, 2], lambda a, b: a + b, 0))

    def test_not_associative(self):
        # subtraction mod 5 has identity-like 0 on the right but is not associative
        self.assertFalse(is_group(range(5), lambda a, b: (a - b) % 5, 0))

    def test_order_divides_group_order(self):
        p = 97
        for g in range(1, p):
            self.assertEqual((p - 1) % order_of(g, p), 0, g)

    def test_known_orders(self):
        self.assertEqual(order_of(1, 97), 1)
        self.assertEqual(order_of(96, 97), 2)  # -1
        self.assertTrue(is_generator(5, 97))
        self.assertFalse(is_generator(96, 97))

    def test_zero_has_no_order(self):
        with self.assertRaises(ValueError):
            order_of(0, 97)

    def test_subgroup(self):
        p = 97
        h = subgroup(96, p)
        self.assertEqual(h, {1, 96})
        g = 5
        self.assertEqual(len(subgroup(g, p)), p - 1)
        # a subgroup is itself a group
        s = subgroup(pow(5, 8, p), p)
        self.assertTrue(is_group(s, lambda a, b: a * b % p, 1))
        self.assertEqual(len(s), order_of(pow(5, 8, p), p))


if __name__ == "__main__":
    unittest.main()
