#!/usr/bin/python3
"""
Defines a funtion that appends a line of text after
a specific line in the file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string.
    """
    with open(filename) as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        updated_lines.append(line)
        if search_string in line:
            updated_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(updated_lines)
