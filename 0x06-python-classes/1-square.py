#!/usr/bin/python3
"""A module containing a class representing a square.

This module defines the Square class, which can be used to create and
perform operations on squares.

Classes:
    Square: A class representing a square.
"""
class Square:
    """A class representing a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(size=0): Initializes the Square object with a specified size.
    """
    def __init__(self, size):
        """Initialize a Square object with the specified size.
        Args:
            size (int): The length of each side of the square.
        """
        self.__size = size
