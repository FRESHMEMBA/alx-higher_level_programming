#!/usr/bin/python3
"""
Defines a class called Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
            print(
                f"{self.print_symbol}" * self.width,
                end='' if i == self.height - 1 else '\n'
            )
        return ""

    def __repr__(self):
        """
        Overrides the __repr__ magic method
        """
        if self.width == 0 or self.height == 0:
            return ""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Overrides the del function
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def square(cls, size=0):
        """
        A square is a rectangle
        """
        return cls(size, size)