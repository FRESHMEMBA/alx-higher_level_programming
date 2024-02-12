#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and
    inherits from the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new instance
            of the Rectangle class.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object
                in the format "[Rectangle] width/height".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
