#!/usr/bin/python3
"""rectangle super class"""


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """ Initialize a Rectangle instance. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Return the string representation of the rectangle. """
        return f"[Rectangle] {self.__width}/{self.__height}"
