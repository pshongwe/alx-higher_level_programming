#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """ Class with public instance method area """
    def area(self):
        """ Raise an exception with a message indicating
that the method is not implemented. """
        raise Exception("area() is not implemented")
