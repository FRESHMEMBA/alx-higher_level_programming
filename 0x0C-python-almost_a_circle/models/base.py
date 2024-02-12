#!/usr/bin/python3
"""
Defines a class named Base.
This class will be the base class of all other classes in this project.
"""


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
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
