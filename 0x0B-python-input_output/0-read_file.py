#!/usr/bin/python3
"""
Defines a function that reads a file and print its content
on the standard output.
"""


def read_file(filename=""):
    """
    Reads the content of a file and prints it.

    Parameters:
    - filename (str): The name of the file to be read.
        If no filename is provided, an empty string is used.

    Returns:
    - None

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
