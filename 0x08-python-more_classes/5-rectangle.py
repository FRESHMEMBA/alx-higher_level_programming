#!/usr/bin/python3
"""
Defines a class called Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Constructor method for the Rectangle class
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

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
        elif value < 0:
            raise ValueError("width must be >= 0")
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Overrides the __str__ magic method
        """
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            print('#' * self.width, end='' if i == self.height - 1 else '\n')
        return ""

    def __repr__(self):
        """
        Overrides the __repr__ magic method
        """
        if self.width == 0 or self.height == 0:
            return ""
        return f"Rectangle({self.width}, {self.height})"

    def __delattr__(self, name):
        """
        Overrides the delattr function
        """
        print("Bye rectangle...")
        super().__delattr__(name)
