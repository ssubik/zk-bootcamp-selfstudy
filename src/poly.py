"""Week 6: polynomial arithmetic over F_p.

A polynomial is a list of coefficients, lowest degree first, with no trailing
zeros. [5, 0, 3] is 3x^2 + 5. The zero polynomial is [].
Run: python3 -m unittest tests.test_poly -v
"""
P = 97


def padd(f, g, p=P):
    raise NotImplementedError


def psub(f, g, p=P):
    raise NotImplementedError


def pmul(f, g, p=P):
    raise NotImplementedError


def peval(f, x, p=P) -> int:
    """Use Horner's rule."""
    raise NotImplementedError


def pdivmod(f, g, p=P):
    """Return (q, r) with f = q*g + r and deg r < deg g.
    Raise ZeroDivisionError when g is the zero polynomial."""
    raise NotImplementedError


def vanishing(xs, p=P):
    """t(x) = product of (x - xi)."""
    raise NotImplementedError


def interpolate(xs, ys, p=P):
    """Lagrange interpolation. Raise ValueError on duplicate x values."""
    raise NotImplementedError
