#!/usr/bin/python3
"""
Defines a function that returns a list of integers that reperesents Pascal's
triangle
"""


def pascal_triangle(n):
    """
    """
    if n <= 0:
        return []
    triangle = [1]
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Calculate each element based on the sum of two elements from the previous row
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return [num for row in triangle for num in row]