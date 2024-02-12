#!/usr/bin/python3
"""
defines a class called Rectangle
"""


Base = __import__("base").Base

class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class"
        """
        super().__init__(id)
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
        if type(value) != int:
            raise TypeError("widht must be an integer")
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
        if type(value) != int:
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
        if type(value) != int:
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
        if type(value) != int:
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
        for h in range(1, self.__height + 1):
            print('#' * self.__width)

    def __str__(self):
        """
        """
        return f"[Rectangle] ({self.__id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
