import unittest
from math_functions import power, divide

class TestGetDataFunctions(unittest.TestCase):

    def test_pow(self):
        self.assertEqual(power(2, 2), 4)

    def test_pow1(self):
        self.assertEqual(power(2, -2), 0.25)
    
    def test_pow2(self):
        self.assertEqual(power(4, 0.5), 2)
    
    def test_pow3(self):
        self.assertEqual(power(5, 0), 1)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)

    def test_divide1(self):
        self.assertIsNone(divide(2, 0))

    def test_divide2(self):
        self.assertEqual(divide(-4, 2), -2)

    def test_divide3(self):
        self.assertEqual(divide(0, 2), 0)

    def test_divide4(self):
        self.assertEqual(divide(-4, -2), 2)


if __name__ == '__main__':
    unittest.main()
