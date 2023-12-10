#!/usr/bin/python3
""" Student class """
class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance."""
        return class_to_json(self)
