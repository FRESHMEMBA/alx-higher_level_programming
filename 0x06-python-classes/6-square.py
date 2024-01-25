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
        position (tuple): The position of the square as a tuple
            of two positive integers.

    Methods:
        __init__(size=0, position=(0, 0)): Initializes the Square object
            with a specified size and position.
        size(): Getter method for the size attribute.
        size(value): Setter method for the size attribute.
        position(): Getter method for the position attribute.
        position(value): Setter method for the position attribute.
        area(): Calculates the area of the square.
        my_print(): Prints a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square object with a specified size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square as a
                tuple of two positive integers.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                of two positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute."""
        if isinstance(value, tuple) and len(value) == 2 and \
           isinstance(value[0], int) and isinstance(value[1], int) and \
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            print('\n' * self.__position[1], end='')
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
