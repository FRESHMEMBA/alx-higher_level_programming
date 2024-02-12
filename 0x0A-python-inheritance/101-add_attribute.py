#!/usr/bin/python3
"""
Defines a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    - obj: The object to which the attribute will be added.
    - attr_name: The name of the attribute to be added.
    - attr_value: The value of the attribute to be added.

    Raises:
    - TypeError: If the object does not have a '__dict__' attribute,
      indicating that attributes cannot be added.

    Returns:
    - None
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
