#!/usr/bin/python3
"""
Defines a function that returns the JSON represenetation of an object (string)
"""


import json

def to_json_string(my_obj):
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
    return json.dumps(my_obj)