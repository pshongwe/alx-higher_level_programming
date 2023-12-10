#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """Returns the dictionary description
for JSON serialization of an object."""
    return obj.__dict__
