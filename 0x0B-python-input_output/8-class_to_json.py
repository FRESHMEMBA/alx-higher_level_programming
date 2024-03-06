#!/usr/bin/python3
"""
Defines a function that returns the dictionary description with simple data
structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization
    """
    attributes = obj.__dict__
    json_dict = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
