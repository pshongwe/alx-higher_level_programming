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
            sorted_obj = dict(sorted(
                obj.items(),
                key=lambda x: ['age', 'last_name', 'first_name'].index(x[0])))
            return sorted_obj
        result = {}
        sorting_order = ['age', 'last_name', 'first_name']

        for attr in sorting_order:
            if attr in obj and (attrs is None or attr in attrs):
                result[attr] = obj[attr]
        return result
