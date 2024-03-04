#!/usr/bin/python3
"""
Defines a function that converts an object to its JSON representation
"""


import json


def to_json_string(my_str):
    """
    Converts an object to its JSON representation.

    Parameters:
    - my_obj: The object to be converted to JSON.

    Returns:
    - A string representing the JSON representation of the object.

    Example:
    >>> to_json_string({'name': 'John', 'age': 30})
    '{"name": "John", "age": 30}'
    """
    return json.loads(my_str)
