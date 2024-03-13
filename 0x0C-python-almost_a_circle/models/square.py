#!/usr/bin/python3
"""
defines a class called Square
"""


# Base = __import__("base").Base
# from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class"
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size attribute
        """
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self._Rectangle__width = value
            self._Rectangle__height = value

    # @property
    # def height(self):
    #     """
    #     Getter method for the height attribute
    #     """
    #     return self._Rectangle__height

    # @height.setter
    # def height(self, value):
    #     """
    #     Setter method for the height attribute
    #     """
    #     if not isinstance(value, int):
    #         raise TypeError("height must be an integer")
    #     elif value <= 0:
    #         raise ValueError("height must be > 0")
    #     else:
    #         self._Rectangle__height = value

    # @property
    # def x(self):
    #     """
    #     Getter method for the x attribute
    #     """
    #     return self._Rectangle__x

    # @x.setter
    # def x(self, value):
    #     """
    #     Setter method for the x attribute
    #     """
    #     if not isinstance(value, int):
    #         raise TypeError("x must be an integer")
    #     elif value < 0:
    #         raise ValueError("x must be >= 0")
    #     else:
    #         self._Rectangle__x = value

    # @property
    # def y(self):
    #     """
    #     Getter method for the y attribute
    #     """
    #     return self._Rectangle__y

    # @y.setter
    # def y(self, value):
    #     """
    #     Setter method for the y attribute
    #     """
    #     if not isinstance(value, int):
    #         raise TypeError("y must be an integer")
    #     elif value < 0:
    #         raise ValueError("y must be >= 0")
    #     else:
    #         self._Rectangle__y = value

    # # def area(self):
    #     """
    #     Computes the area of a rectangle
    #     """
    #     return self._Rectangle__width * self._Rectangle__height

    # def display(self):
    #     """
    #     Displays a rectangle on the screen
    #     """
    #     print('\n' * self._Rectangle__x, end='')
    #     for _ in range(self._Rectangle__height):
    #         print(' ' * self._Rectangle__y + '#' * self._Rectangle__width)

    def update(self, *args, **kwargs):
        """
        Updates the values of the attributes of this object
        """
        nargs = len(args)

        if nargs != 0:
            if nargs >= 1:
                self.id = args[0]
            if nargs >= 2:
                self._Rectangle__width = args[1]
                self._Rectangle__height = args[1]
            if nargs >= 3:
                self._Rectangle__x = args[2]
            if nargs >= 4:
                self._Rectangle__y = args[3]
        elif kwargs is not None:
            kwargs_keys = kwargs.keys()
            if "id" in kwargs_keys:
                self.id = kwargs["id"]
            if "size" in kwargs_keys:
                self._Rectangle__height = kwargs["size"]
                self._Rectangle__width = kwargs["size"]
            if 'x' in kwargs_keys:
                self._Rectangle__x = kwargs['x']
            if 'y' in kwargs_keys:
                self._Rectangle__y = kwargs['y']

    def __str__(self, name="Square"):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string containing the following info about the Square:
                - The id of the Square.
                - The x-coordinate of the Square's position.
                - The y-coordinate of the Square's position.
                - The width of the Square.
        """
        return "[{name}] ({}) {}/{} - {}".format(
            self.id,
            self._Rectangle__x,
            self._Rectangle__y,
            self._Rectangle__width,
            )

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object.

        Returns:
            dict: A dictionary containing the attributes of the Square object.
                - "id" (int): The id of the Square.
                - "x" (int): The x-coordinate of the Square's position.
                - "size" (int): The size of the Square.
                - "y" (int): The y-coordinate of the Square's position.
        """
        return {
            "id": self.id,
            'x': self._Rectangle__x,
            "size": self.size,
            'y': self._Rectangle__y,
            }
