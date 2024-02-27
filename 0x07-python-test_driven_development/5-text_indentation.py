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
    
    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[i], end="\n\n")
            i += 1
            continue
        if text[i] == ' ' and text[i - 1] in ".?:":
            continue
        print(text[i], end='')