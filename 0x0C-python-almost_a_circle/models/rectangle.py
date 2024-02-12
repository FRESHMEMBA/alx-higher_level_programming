#!/usr/bin/python3
"""
defines a class called Rectangle
"""


import Base

class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class"
        """
        self.super(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
