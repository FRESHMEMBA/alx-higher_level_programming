#!/usr/bin/python3
class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0,0)):
        """Initialize the Square object with a specified size."""
        self.__size = size
        self.__position = position
    
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
        return self.__position
    
    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
    
    def my_print(self):
        """Prints a square."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)