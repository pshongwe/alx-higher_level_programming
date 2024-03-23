#!/usr/bin/python3
""" Base class """
import json
import os
import csv


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

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                raise TypeError("Unknown class")

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                raise TypeError("Unknown class")

            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            next(reader)  # Skip header
            return [cls.create(**{k: int(v) for k, v in row.items()})
                    for row in reader]
