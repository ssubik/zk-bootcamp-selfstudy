"""Week 5: rank-1 constraint systems.

Run: python3 -m unittest tests.test_r1cs -v
"""
P = 97


def is_satisfied(L, R, O, w, p=P) -> bool:
    """True when (L.w) * (R.w) == (O.w) for every row, mod p.
    Raise ValueError if any row length differs from len(w) or the
    matrices have different numbers of rows."""
    raise NotImplementedError


def cubic_r1cs(p=P):
    """Return (L, R, O) for out = x^3 + x + 5 using exactly two constraints.
    Witness layout: w = [1, out, x, v1] where v1 = x * x."""
    raise NotImplementedError


def cubic_witness(x: int, p=P) -> list:
    """Return the witness [1, out, x, v1] for input x."""
    raise NotImplementedError
