#!/usr/bin/python3
"""Student class."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained in this
        list are retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                            for item in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
