#!/usr/bin/python3
"""
Defines a class named Base.
This class will be the base class of all other classes in this project.
"""


import json


class Base:
    """
    Base class for all other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor for the Base class.
        """
        # self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the json represenatation of an object
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
