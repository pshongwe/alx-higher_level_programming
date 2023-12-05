#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """ Return True if obj is an instance of a class
that inherited from a_class; otherwise False. """
    return isinstance(obj, a_class) and type(obj) != a_class
