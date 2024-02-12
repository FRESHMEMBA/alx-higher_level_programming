#!/usr/bin/python3
"""
Defines a funtion that returns a list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: The object to look up.

    Returns:
    - A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
