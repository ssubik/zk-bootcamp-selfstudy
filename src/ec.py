"""Week 3: elliptic curve arithmetic from scratch.

Curve y^2 = x^3 + A*x + B over F_P. Points are (x, y) tuples; the point at
infinity is INF (None). Every public function must raise ValueError when given
a point that is not on the curve.
Run: python3 -m unittest tests.test_ec -v
"""
P = 101
A = 0
B = 3
INF = None


def is_on_curve(pt, p=P, a=A, b=B) -> bool:
    raise NotImplementedError


def neg(pt, p=P, a=A, b=B):
    raise NotImplementedError


def add(p1, p2, p=P, a=A, b=B):
    """Handle: INF on either side, P + (-P), doubling (including y = 0)."""
    raise NotImplementedError


def scalar_mul(k: int, pt, p=P, a=A, b=B):
    """Double-and-add. Negative k means (-k) * (-pt)."""
    raise NotImplementedError


def all_points(p=P, a=A, b=B) -> list:
    """Every point on the curve, including INF."""
    raise NotImplementedError
