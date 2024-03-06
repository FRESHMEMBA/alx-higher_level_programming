#!/usr/bin/python3
"""
Defines a function that returns a list of integers that reperesents Pascal's
triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers that represents Pascal's triangle up to the given number of rows.

    Parameters:
    - n (int): The number of rows in Pascal's triangle to generate.

    Returns:
    - List[int]: A list of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return [num for num in triangle[-1]]
