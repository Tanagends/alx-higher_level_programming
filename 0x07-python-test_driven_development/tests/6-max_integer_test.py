#!/usr/bin/python3
"""Unittest for ``max_integer([..])``
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for ``max_integer([..])"""

    def test_ordered(self):
        """Test ordered list"""
        olist = [1, 2, -3, 4, 5]
        self.assertEqual(max_integer(olist), 5)

    def test_unordered(self):
        """Test unordered list"""
        ulist = [3, 5, 1, 2, -4]
        self.assertEqual(max_integer(ulist), 5)

    def test_empty(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single(self):
        """Test single element list"""
        self.assertEqual(max_integer([1]), 1)

    def test_at_beginning(self):
        """Test max at beginning"""
        self.assertEqual(max_integer([4.2, 3, -9]), 4.2)

    def test_floats(self):
        """Test a list of floating point numbers"""
        floats = [1.1, -2.2, 3.3, 4.1, 4.2]
        self.assertEqual(max_integer(floats), 4.2)

    def test_mix(self):
        """Test a mixed list of floats and ints"""
        mixed = [1, 2.3, 3.1, -4, 4.5, 5.1, 6]
        self.assertEqual(max_integer(mixed), 6)

    def test_str(self):
        """Test string"""
        self.assertEqual(max_integer("Amro"), 'r')

    def test_strlist(self):
        """Test list of strings"""
        slist = ["Amro", "Mohamed", "Sati"]
        self.assertEqual(max_integer(slist), 'Sati')

    def test_empty_str(self):
        """Test empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
