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

    def to_json(self):
        """
        Retrieves a dictionary represenatation of a Student instance
        """
        attributes = self.__dict__
        json_dict = {}

        for key, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value

        return json_dict
