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

    def test_invalid_input(self):
        """
        """
        # self.assertRaises(TypeError, max_integer(["one", 2]))
        # self.assertRaises(TypeError, max_integer([1, True]))

    def test_valid_input(self):
        """
        """
        self.assertEqual(5, max_integer([5]))
        self.assertEqual(7, max_integer([1, 3, 5, 7]))

    