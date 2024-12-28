# test_fibonacci.py

import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        # Test the first 5 Fibonacci numbers
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_zero_input(self):
        # Test when n is 0
        self.assertEqual(fibonacci(0), [])

    def test_one_input(self):
        # Test when n is 1
        self.assertEqual(fibonacci(1), [0])

    def test_large_input(self):
        # Test for a larger Fibonacci sequence
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == "__main__":
    unittest.main()
