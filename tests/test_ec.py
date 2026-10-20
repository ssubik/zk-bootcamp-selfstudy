"""Week 3 tests. Run: python3 -m unittest tests.test_ec -v

Curve: y^2 = x^3 + 3 over F_101 (same shape as BN254, tiny prime).
"""
import itertools
import unittest

from src.ec import P, INF, is_on_curve, neg, add, scalar_mul, all_points


class TestEC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pts = all_points()
        cls.affine = [q for q in cls.pts if q is not INF]

    def test_point_count(self):
        # p = 101 is 2 mod 3, so this curve has exactly p + 1 points (incl. INF)
        self.assertEqual(len(self.pts), P + 1)
        self.assertIn(INF, self.pts)

    def test_points_on_curve(self):
        for q in self.pts:
            self.assertTrue(is_on_curve(q))
        self.assertFalse(is_on_curve((0, 0)))

    def test_identity_and_inverse(self):
        for q in self.pts:
            self.assertEqual(add(q, INF), q)
            self.assertEqual(add(INF, q), q)
            self.assertEqual(add(q, neg(q)), INF)

    def test_doubling_point_with_y_zero(self):
        twos = [q for q in self.affine if q[1] == 0]
        self.assertTrue(twos, "curve should have a 2-torsion point")
        for q in twos:
            self.assertEqual(add(q, q), INF)

    def test_closure_and_commutativity(self):
        for a, b in itertools.product(self.pts[:30], repeat=2):
            c = add(a, b)
            self.assertTrue(is_on_curve(c))
            self.assertEqual(c, add(b, a))

    def test_associativity(self):
        sample = self.pts[:15]
        for a, b, c in itertools.product(sample, repeat=3):
            self.assertEqual(add(add(a, b), c), add(a, add(b, c)))

    def test_scalar_mul_matches_repeated_addition(self):
        g = self.affine[0]
        acc = INF
        for k in range(0, 40):
            self.assertEqual(scalar_mul(k, g), acc, k)
            acc = add(acc, g)

    def test_group_order_kills_every_point(self):
        n = len(self.pts)
        for q in self.pts:
            self.assertEqual(scalar_mul(n, q), INF)

    def test_homomorphism(self):
        g = self.affine[3]
        for a, b in [(5, 7), (50, 60), (101, 1)]:
            self.assertEqual(add(scalar_mul(a, g), scalar_mul(b, g)), scalar_mul(a + b, g))

    def test_negative_scalar(self):
        g = self.affine[1]
        self.assertEqual(scalar_mul(-3, g), neg(scalar_mul(3, g)))

    def test_prime_order_subgroup_exists(self):
        # 102 = 2 * 3 * 17: multiplying by the cofactor 6 lands in the order-17 subgroup
        found = False
        for q in self.affine:
            h = scalar_mul(6, q)
            if h is not INF:
                self.assertEqual(scalar_mul(17, h), INF)
                found = True
        self.assertTrue(found)

    def test_rejects_points_off_curve(self):
        bad = (0, 0)
        for f in (lambda: add(bad, INF), lambda: neg(bad), lambda: scalar_mul(2, bad)):
            with self.assertRaises(ValueError):
                f()


if __name__ == "__main__":
    unittest.main()
