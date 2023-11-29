#!/usr/bin/python3
"""Defines integer addition function."""

def add_integer(a, b=98):
    """
    This function adds two integers or floats.
    The floats are casted to integers before addition.
    Raises TypeError if a or b is neither an integer nor a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    
    return a + b
