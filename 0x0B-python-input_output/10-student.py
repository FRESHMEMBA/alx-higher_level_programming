#!/usr/bin/python3
"""
Defines a class that defines a student
"""


class Student:
    """
    A class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor method for the student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary represenatation of a Student instance
        """
        types = (list, dict, str, int, bool)
        attributes = self.__dict__
        json_dict = {}

        if attrs is None:
            for key, value in attributes.items():
                if isinstance(value, types):
                    json_dict[key] = value
        elif isinstance(attrs, list):
            for attr in attrs:
                if attr in attributes and isinstance(attributes[attr], types):
                    json_dict[attr] = attributes[attr]
        return json_dict
