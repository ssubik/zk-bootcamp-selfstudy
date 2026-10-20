"""Week 7: R1CS to QAP. Builds on src/r1cs.py and src/poly.py.

Interpolate each matrix column over the domain x = 1..n (n = number of rows).
Run: python3 -m unittest tests.test_qap -v
"""
from src.poly import P  # noqa: F401  (import padd, pmul, ... as you need them)


def r1cs_to_qap(L, R, O, p=P):
    """Return (U, V, W, t): one polynomial per witness column for each matrix,
    and the vanishing polynomial t of the domain."""
    raise NotImplementedError


def combine(polys, w, p=P):
    """sum_i w[i] * polys[i]"""
    raise NotImplementedError


def quotient(U, V, W, t, w, p=P):
    """Return h with (U.w)(V.w) - (W.w) = h * t.
    Raise ValueError when the division leaves a remainder (invalid witness)."""
    raise NotImplementedError
