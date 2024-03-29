#!/usr/bin/python3
"""
defines a class called Rectangle
"""


# Base = __import__("base").Base
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class"
        """
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Computes the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays a rectangle on the screen
        """
        print('\n' * self.__y, end='')
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)
        # print('\n' * self.__x, end='')
        # for _ in range(1, self.__height + 1):
        #     print(' ' * self.__y + '#' * self.__width)

    def update(self, *args, **kwargs):
        """
        Updates the values of the attributes of this object
        """
        nargs = len(args)

        if nargs != 0:
            if nargs >= 1:
                self.id = args[0]
            if nargs >= 2:
                self.__width = args[1]
            if nargs >= 3:
                self.__height = args[2]
            if nargs >= 4:
                self.__x = args[3]
            if nargs >= 5:
                self.__y = args[4]
        elif kwargs is not None:
            kwargs_keys = kwargs.keys()
            if "id" in kwargs_keys:
                self.id = kwargs["id"]
            if "height" in kwargs_keys:
                self.__height = kwargs["height"]
            if "width" in kwargs_keys:
                self.__width = kwargs["width"]
            if 'x' in kwargs_keys:
                self.__x = kwargs['x']
            if 'y' in kwargs_keys:
                self.__y = kwargs['y']

    def __str__(self):
        """
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
            )

    def to_dictionary(self):
        """
        """
        return {
            'x': self.__x,
            'y': self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width
            }
