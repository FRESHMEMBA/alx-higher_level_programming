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
        
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
