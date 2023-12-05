#!/usr/bin/python3
"""square class"""


class Square(Rectangle):
    """ Square class that inherits from Rectangle. """

    def __init__(self, size):
        """ Initialize a Square instance. """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
