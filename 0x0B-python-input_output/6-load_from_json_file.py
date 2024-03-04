#!/usr/bin/python3
"""
Defines a funtion that creates an Object from a JSON file.
"""


import json


def load_from_json(filename):
    """
    Loads data from a JSON file and returns it as a Python object.

    Parameters:
    - filename (str): The name of the JSON file to load.

    Returns:
    - object: The Python object representing the data in the JSON file.

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    - JSONDecodeError: If the file contains invalid JSON data.

    Example:
        >>> load_from_json('data.json')
        {'name': 'John', 'age': 30, 'city': 'New York'}
    """
    with open(filename) as file:
        return json.load(file)
