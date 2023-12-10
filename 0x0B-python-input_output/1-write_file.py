#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
        return characters_written
