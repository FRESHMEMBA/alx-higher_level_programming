#!/usr/bin/python3
"""
Defines a custom list class that inherits from the built-in list class.

This class provides an additional method, print_sorted, which prints
the elements of the list in sorted order.

Attributes:
        None

Methods:
    print_sorted: Prints the elements of the list in sorted order.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    This class provides an additional method, print_sorted,
    which prints the elements of the list in sorted order.

    Methods:
    - print_sorted: Prints the elements of the list in sorted order.

    Inherited Methods:
    - append: Appends an element to the end of the list.
    - extend: Extends the list by appending elements from an iterable.
    - insert: Inserts an element at a specified position in the list.
    - remove: Removes the first occurrence of a specified
        element from the list.
    - pop: Removes and returns the element at a specified
        position in the list.
    - clear: Removes all elements from the list.
    - index: Returns the index of the first occurrence of a specified
        element in the list.
    - count: Returns the number of occurrences of a specified
        element in the list.
    - sort: Sorts the elements of the list in place.
    - reverse: Reverses the order of the elements in the list.
    - copy: Returns a shallow copy of the list.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Parameters:
             self (MyList): The instance of MyList class.

        Returns:
            None
        """
        print(sorted(self))
