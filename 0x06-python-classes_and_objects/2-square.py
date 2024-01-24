#!/usr/bin/python3
class Square:
    """A class representing a square
    """
    def __init__(self, size):
        """Initialize a Square object with the specified size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
