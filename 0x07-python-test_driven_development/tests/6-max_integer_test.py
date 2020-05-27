#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Perfom unittest class
    """
    def tests_max(self):
        self.assertEqual(max_integer([1, 10, 5]), 10)

    def tests_max_zero(self):
        self.assertEqual(max_integer([0, -1, -5]), 0)

    def tests_max_empty(self):
        self.assertEqual(max_integer([]), None)

    def tests_max_one(self):
        self.assertEqual(max_integer([2]), 2)

    def tests_max_same(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def tests_max_str(self):
        self.assertEqual(max_integer("abc"), 'c')


if __name__ == '__main__':
    unittest.main()