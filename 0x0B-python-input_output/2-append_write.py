#!/usr/bin/python3
"""
Defines a funtion that appends text to a file
"""


def append_write(filename="", text=""):
    """
    Appends content to a file.

    Parameters:
    - file_path (str): The path to the file to be written.
    - content (str): The content to be written to the file.

    Returns:
    - None

    Raises:
    - FileNotFoundError: If the specified file path does not exist.
    - PermissionError: If the user does not have permission
        to write to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
