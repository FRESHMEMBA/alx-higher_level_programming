#!/usr/bin/python3
"""
Defines an empty class called BaseGeometry
"""


class BaseGeometry():
    """
    This is the BaseGeometry class.

    It serves as a base class for other geometry classes.

    Attributes:
        None

    Methods:
        area
        integer_validator
    """
    def area(self):
        """
        Calculate the area of the geometry.

        This method is not implemented in the BaseGeometry class and should be
        overridden in the derived classes.

        Parameters:
            self (BaseGeometry): The instance of the BaseGeometry class.

        Raises:
            Exception: This method is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate an integer value.

        This method checks if the given value is an integer and greater than 0

        Parameters:
            self (BaseGeometry): The instance of the BaseGeometry class.
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
