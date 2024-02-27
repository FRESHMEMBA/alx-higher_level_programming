#!/usr/bin/python3
"""
Defines a function that prints a sqaure with the character #.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Parameters:
    - size (int): The size of the square. Must be a non-negative integer.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    else:
        for _ in range(size):
            print('#' * size)
