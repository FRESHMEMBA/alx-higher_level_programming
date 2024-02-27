#!/usr/bin/python3
"""Unit test for max_integer([..])
"""


import unittest

max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """
    """
    def test_empty_list(self):
        """
        """
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(2, max_integer([2]))

    def test_max_begining(self):
        """
        """
        self.assertEqual(5, max_integer([5, 3, 1, 2]))

    def test_max_middle(self):
        self.assertEqual(10, max_integer([2, 5, 10, 1, 7]))

    def test_max_end(self):
        self.assertEqual(7, max_integer([1, 3, 5, 7]))

    def test_negative_numbers(self):
        self.assertEqual(-1, max_integer([-4, -3, -2, -1]))

    