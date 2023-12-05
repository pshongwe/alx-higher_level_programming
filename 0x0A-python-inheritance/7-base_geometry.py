#!/usr/bin/python3
"""base geometry"""


class BaseGeometry:
    """ Class with public instance methods area and integer_validator """

    def area(self):
        """ Raise an exception indicating that
the method is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate that value is a positive integer. """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
