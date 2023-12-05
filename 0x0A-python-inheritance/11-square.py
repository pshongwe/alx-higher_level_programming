#!/usr/bin/python3
"""square class"""


class Square(Rectangle):
    """ Square class that inherits from Rectangle. """

    def __init__(self, size):
        """ Initialize a Square instance. """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Return the string representation of the square. """
        return f"[Square] {self.__size}/{self.__size}"
