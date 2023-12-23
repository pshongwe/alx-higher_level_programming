#!/usr/bin/python3
""" define Student class """


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        obj = self.__dict__.copy()
        if not attrs:  # If attrs is None, return the whole dictionary
            return obj
        if not all(isinstance(attr, str) for attr in attrs):
            return obj
        return {attr: obj[attr] for attr in attrs if attr in obj}

    def reload_from_json(self, json):
        """Replace attributes of the Student object with
values from JSON dictionary."""
    for key, value in json.items():
        setattr(self, key, value)
