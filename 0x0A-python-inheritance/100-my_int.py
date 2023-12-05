#!/usr/bin/python3
"""My Int"""


class MyInt(int):
    """ MyInt is a rebel class that inverts == and != operators. """

    def __eq__(self, other):
        """ Invert the == operator. """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Invert the != operator. """
        return super().__eq__(other)
