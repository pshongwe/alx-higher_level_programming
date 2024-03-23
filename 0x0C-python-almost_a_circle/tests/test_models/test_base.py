#!/usr/bin/python3
"""Base class unit tests """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Set up method to reset the number of objects before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatic ID assignment."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_auto_id_increment(self):
        """Test automatic ID increment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_manual_id(self):
        """Test manual ID assignment."""
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string_none(self):
        """Test conversion of None to JSON string."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_empty_list(self):
        """Test conversion of an empty list to JSON string."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_list_dict(self):
        """Test conversion of a list of dictionaries to JSON string."""
        json_str = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_str, '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test conversion of None from JSON string."""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty(self):
        """Test conversion of an empty string from JSON string."""
        list_output = Base.from_json_string("[]")
        self.assertEqual(list_output, [])

    def test_from_json_string_list(self):
        """Test conversion of a JSON string to a list."""
        list_output = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(list_output, [{"id": 89}])


if __name__ == "__main__":
    unittest.main()
