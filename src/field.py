"""Week 1: arithmetic in the prime field F_p.

Replace every NotImplementedError. Every function must accept negative or
oversized inputs and return a value in [0, p).
Run: python3 -m unittest tests.test_field -v
"""
P = 97


def add(a: int, b: int, p: int = P) -> int:
    raise NotImplementedError


def sub(a: int, b: int, p: int = P) -> int:
    raise NotImplementedError


def neg(a: int, p: int = P) -> int:
    raise NotImplementedError


def mul(a: int, b: int, p: int = P) -> int:
    raise NotImplementedError


def inv(a: int, p: int = P) -> int:
    """Inverse via Fermat's little theorem: a^(p-2).
    Raise ZeroDivisionError when a % p == 0."""
    raise NotImplementedError


def inv_euclid(a: int, p: int = P) -> int:
    """Inverse via the extended Euclidean algorithm (do not call pow).
    Raise ZeroDivisionError when a % p == 0."""
    raise NotImplementedError


def div(a: int, b: int, p: int = P) -> int:
    raise NotImplementedError
