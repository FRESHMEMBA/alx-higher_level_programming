#!/usr/bin/python3
"""
Defines a function that prints a text with 2 new lines after each of these
characters: ., ?, and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of the characters '.', '?', and ':'.

    Parameters:
    text (str): The text to be printed.

    Raises:
    TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for c in text:
        print(c, end='' if c not in ".?:" else "\n\n")