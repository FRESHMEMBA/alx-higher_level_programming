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
        size(): Getter method for the size attribute.
        size(value): Setter method for the size attribute.
        area(): Calculates the area of the square.
        my_print(): Prints a square.
    """

    def __init__(self, size=0):
        """Initialize the Square object with a specified size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
