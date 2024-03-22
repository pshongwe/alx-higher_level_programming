#!/usr/bin/python3
""" test max integer """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define novel unittests for max_integer([..])."""

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        negatives = [-10, -20, -30, -40]
        self.assertEqual(max_integer(negatives), -10)

    def test_max_in_middle(self):
        """Test a list where the max value is in the middle."""
        max_in_middle = [1, 2, 50, 4, 5]
        self.assertEqual(max_integer(max_in_middle), 50)

    def test_same_elements(self):
        """Test a list where all elements are the same."""
        same_elements = [7, 7, 7, 7]
        self.assertEqual(max_integer(same_elements), 7)

    def test_single_negative_element(self):
        """Test a list with a single negative element."""
        single_negative = [-5]
        self.assertEqual(max_integer(single_negative), -5)

    def test_large_numbers(self):
        """Test a list with very large numbers."""
        large_numbers = [999999, 888888, 777777, 1000000]
        self.assertEqual(max_integer(large_numbers), 1000000)

    def test_mixed_types(self):
        """Test a list with mixed types (integers and strings)."""
        mixed_types = [1, '2', 3, '4']
        with self.assertRaises(TypeError):
            max_integer(mixed_types)

    def test_none_in_list(self):
        """Test a list containing None."""
        list_with_none = [1, 2, None, 3]
        with self.assertRaises(TypeError):
            max_integer(list_with_none)

    def test_boolean_values(self):
        """Test a list with boolean values."""
        bools = [True, False, True, False]
        self.assertEqual(max_integer(bools), True)

if __name__ == '__main__':
    unittest.main()
