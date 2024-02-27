#!/usr/bin/python3
"""
Defines a class called LockedClass
"""


class LockedClass:
    """
    Class LockedClass prevents the user from dynamically creating new instance
    attributes, except if the new attribute is called first_name
    """
    __slots__ = ["first_name"]
    def __setattr__(self, name, value):
        """
        Overrides the setattr function
        """
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
                )