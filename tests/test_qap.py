"""Week 7 tests. Run: python3 -m unittest tests.test_qap -v

Uses your Week 5 R1CS (src/r1cs.py) and Week 6 polynomials (src/poly.py).
Interpolation points are x = 1..n for n constraints.
"""
import unittest

from src.poly import P, padd, psub, pmul, peval
from src.r1cs import cubic_r1cs, cubic_witness
from src.qap import r1cs_to_qap, combine, quotient


class TestQAP(unittest.TestCase):
    def setUp(self):
        self.L, self.R, self.O = cubic_r1cs()
        self.U, self.V, self.W, self.t = r1cs_to_qap(self.L, self.R, self.O)

    def test_columns_interpolate_matrix(self):
        n = len(self.L)
        for M, polys in ((self.L, self.U), (self.R, self.V), (self.O, self.W)):
            self.assertEqual(len(polys), len(M[0]))
            for j, f in enumerate(polys):
                for i in range(n):
                    self.assertEqual(peval(f, i + 1), M[i][j] % P)

    def test_t_vanishes_on_domain(self):
        for x in range(1, len(self.L) + 1):
            self.assertEqual(peval(self.t, x), 0)

    def test_valid_witness_divides(self):
        for x in (2, 3, 41):
            w = cubic_witness(x)
            h = quotient(self.U, self.V, self.W, self.t, w)
            u, v, ww = (combine(M, w) for M in (self.U, self.V, self.W))
            self.assertEqual(psub(pmul(u, v), ww), pmul(h, self.t))

    def test_invalid_witness_rejected(self):
        w = cubic_witness(3)
        w[1] = (w[1] + 1) % P
        with self.assertRaises(ValueError):
            quotient(self.U, self.V, self.W, self.t, w)

    def test_schwartz_zippel_spot_check(self):
        # the identity also holds at a random point outside the domain
        w = cubic_witness(5)
        h = quotient(self.U, self.V, self.W, self.t, w)
        u, v, ww = (combine(M, w) for M in (self.U, self.V, self.W))
        tau = 77
        lhs = (peval(u, tau) * peval(v, tau) - peval(ww, tau)) % P
        self.assertEqual(lhs, peval(h, tau) * peval(self.t, tau) % P)


if __name__ == "__main__":
    unittest.main()
