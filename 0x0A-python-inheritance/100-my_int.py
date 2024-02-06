#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class that represents an integer with modified equality operators.

    This class inherits from the built-in int class and overrides the __eq__ and __ne__ methods to provide a modified behavior for equality comparisons.

    Attributes:
        None

    Methods:
        __eq__(self, other): Overrides the equality operator (==) to return the result of the inequality operator (!=) of the super class.
        __ne__(self, other): Overrides the inequality operator (!=) to return the result of the equality operator (==) of the super class.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to return the result of the inequality operator (!=) of the super class.

        Parameters:
            other (object): The object to compare with.

        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        return super().__ne__(other)
    
    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to return the result of the equality operator (==) of the super class.

        Parameters:
            other (object): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return super().__eq__(other)
