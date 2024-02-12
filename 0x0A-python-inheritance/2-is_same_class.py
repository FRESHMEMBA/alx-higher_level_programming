#!/usr/bin/python3
"""
Defines a function that returns True if the object is exactly an instance of
the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is an instance of the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare against.

    Returns:
    - True if the object is exactly an instance of the specified class;
        otherwise False.
    """
    return type(obj) == a_class
