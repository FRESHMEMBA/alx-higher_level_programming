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

    @property
    def width(self):
        """
        Getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute
        """
        self.__x = value

    @property
    def y(self)
    """
    Getter method for the y attribute
    """
    return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute
        """
        self.__y = value
