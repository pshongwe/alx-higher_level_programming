#!/usr/bin/python3
""" Base class """
import json


class Base:
    """class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize it"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string
        representation of list_dictionaries."""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        if list_objs:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dictionaries = []
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        # Create a "dummy" instance with default values
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise TypeError("Unknown class type")

        # Update the "dummy" instance with the real values
        dummy_instance.update(**dictionary)
        return dummy_instance
