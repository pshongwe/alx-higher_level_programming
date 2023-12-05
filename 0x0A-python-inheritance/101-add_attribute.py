#!/usr/bin/python3
"""add attribute """


def add_attribute(obj, attr, value):
    """ Add a new attribute to an object if possible. """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
