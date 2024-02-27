#!/usr/bin/python3
"""
Defines a function named add_integer that adds two integers
"""

def add_integer(a, b=98):
    """
    Returns the sum of two numbers, a and b.
    
    Parameters:
    a (int or float): The first number to be added.
    b (int or float, optional): The second number to be added. Defaults to 98.
    
    Returns:
    int: The sum of a and b.
    
    Raises:
    TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)

    return a + b