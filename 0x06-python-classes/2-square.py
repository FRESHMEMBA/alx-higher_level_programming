#!/usr/bin/python3
"""A module containing a class representing a square.

This module defines the Square class, which can be used to create and
perform operations on squares.

Classes:
    Square: A class representing a square.
"""
class Square:
    """A class representing a square
    """
    def __init__(self, size):
        """Initialize a Square object with the specified size.
        Args:
            size (int): The length of each side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
