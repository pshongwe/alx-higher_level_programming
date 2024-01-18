#!/usr/bin/python3
"""
This module provides a function to add two numbers.
It includes handling for different data types and error checking.
The primary function is add_integer.
"""


def add_integer(a, b=98):
    """
    Adds two numbers, casting floats to integers.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    aa = int(a)
    bb = int(b)
    return aa + bb
