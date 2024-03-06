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
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize each row with 1
        if i >= 2:
            for j in range(1, i):
                # Calculate each element based on the sum of two elements from the previous row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
