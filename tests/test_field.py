import unittest
from src.field import add, mul, inv, div

class TestField(unittest.TestCase):
    def test_add_wrap(self): self.assertEqual(add(96, 2), 1)
    def test_mul_wrap(self): self.assertEqual(mul(15, 10), 53)
    def test_inverse(self): self.assertEqual(mul(5, inv(5)), 1)
    def test_div(self): self.assertEqual(div(15, 5), 3)
    def test_zero(self):
        with self.assertRaises(ZeroDivisionError): inv(0)

if __name__ == '__main__': unittest.main()
