"""Week 6 tests. Run: python3 -m unittest tests.test_poly -v

Polynomials are coefficient lists, lowest degree first, no trailing zeros.
The zero polynomial is [].
"""
import random
import unittest

from src.poly import P, padd, psub, pmul, peval, pdivmod, vanishing, interpolate


class TestPoly(unittest.TestCase):
    def test_add_sub_trim(self):
        self.assertEqual(padd([1, 2, 3], [1, 2, P - 3]), [2, 4])
        self.assertEqual(psub([1, 2], [1, 2]), [])

    def test_mul(self):
        # (x + 1)(x - 1) = x^2 - 1
        self.assertEqual(pmul([1, 1], [P - 1, 1]), [P - 1, 0, 1])
        self.assertEqual(pmul([], [1, 2]), [])

    def test_eval(self):
        f = [5, 0, 3]  # 3x^2 + 5
        self.assertEqual(peval(f, 2), 17)
        self.assertEqual(peval([], 9), 0)

    def test_divmod_roundtrip(self):
        rng = random.Random(7)
        for _ in range(50):
            f = [rng.randrange(P) for _ in range(rng.randrange(1, 9))] + [1]
            g = [rng.randrange(P) for _ in range(rng.randrange(1, 4))] + [rng.randrange(1, P)]
            q, r = pdivmod(f, g)
            self.assertLess(len(r), len(g))
            self.assertEqual(padd(pmul(q, g), r), f)

    def test_divide_by_zero_poly(self):
        with self.assertRaises(ZeroDivisionError):
            pdivmod([1, 2], [])

    def test_vanishing(self):
        t = vanishing([1, 2, 3])
        for x in (1, 2, 3):
            self.assertEqual(peval(t, x), 0)
        self.assertNotEqual(peval(t, 4), 0)
        self.assertEqual(len(t), 4)

    def test_interpolate_hits_points(self):
        xs, ys = [1, 2, 3, 4], [7, 0, 96, 13]
        f = interpolate(xs, ys)
        self.assertLessEqual(len(f), len(xs))
        for x, y in zip(xs, ys):
            self.assertEqual(peval(f, x), y)

    def test_interpolate_is_unique(self):
        f = [3, 1, 4, 1]
        xs = [5, 9, 2, 6]
        self.assertEqual(interpolate(xs, [peval(f, x) for x in xs]), f)

    def test_interpolate_duplicate_x(self):
        with self.assertRaises(ValueError):
            interpolate([1, 1], [2, 3])

    def test_divisible_iff_roots(self):
        # f vanishes on {1,2,3} exactly when t divides it with zero remainder
        t = vanishing([1, 2, 3])
        f = pmul(t, [4, 5])
        self.assertEqual(pdivmod(f, t)[1], [])
        self.assertNotEqual(pdivmod(padd(f, [1]), t)[1], [])


if __name__ == "__main__":
    unittest.main()
