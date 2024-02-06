#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class or if it
    is an instance of a class that inherited from the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to be checked against.

    Returns:
    - True if the object is an instance of the specified class or if it is an
        instance of a class that inherited from the specified class.
    - False otherwise.
    """
    return isinstance(obj, a_class)
