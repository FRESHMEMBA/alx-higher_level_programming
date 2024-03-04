#!/usr/bin/python3
"""
Defines a funtion that writes an Object to a text file,
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Parameters:
    - my_obj: The object to be written to the file.
    - filename: The name of the file to write the object to.

    Returns:
    None

    Raises:
    - TypeError: If the object cannot be serialized to JSON.
    - FileNotFoundError: If the file specified by the filename does not exist.

    Example:
    save_to_json_file({"name": "John", "age": 30}, "data.json")
    """
    with open(filename) as file:
        json.dump(my_obj, file)