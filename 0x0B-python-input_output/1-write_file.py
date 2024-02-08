#!/usr/bin/python3
"""
Defines a funtion that writes text to a file
"""


def write_file(filename="", text=""):
    """
    Writes content to a file.

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
    with open(filename, 'w', unicode="utf-8") as file:
        return file.write(text)
