#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 5, 7]), 7)
        self.assertEqual(max_integer([3, 5, 9, 1]), 9)
        self.assertEqual(max_integer([-1, -3, -5, -9]), -1)
        self.assertEqual(max_integer([1.45, 15.5, 10, -2]), 15.5)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
