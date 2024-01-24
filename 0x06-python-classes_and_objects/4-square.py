class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize the Square object with a specified size."""
        self.__size = size
    
    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
