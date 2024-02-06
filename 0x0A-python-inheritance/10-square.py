#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines a class Square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new instance of the Square class.
        area(self): Calculates the area of the square.
        __str__(self): Returns a string representation of the square.
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square.

        Returns:
            None

        Raises:
            None
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.

        Raises:
            None
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.

        Raises:
            None
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
