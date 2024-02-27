#!/usr/bin/python3
"""
Defines a function that divides all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all the elements of a matrix by a given divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided. Each element of the matrix should be an integer or a float.
    - div (int or float): The divisor to divide the matrix elements by.

    Returns:
    - matrix_div (list of lists): The resulting matrix after dividing each element by the divisor. Each element of the resulting matrix will be rounded to 2 decimal places.

    Raises:
    - TypeError: If the matrix is not a list of lists, or if any element of the matrix is not an integer or a float.
    - TypeError: If the rows of the matrix do not have the same size.
    - ZeroDivisionError: If the divisor is zero.
    """
    matrix_div = []
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats."
            )

    if len(set(map(lambda row: len(row), matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        matrix_row = []
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

            try:
                matrix_row.append(round(n / div, 2))
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")

        matrix_div.append(matrix_row)
    return matrix_div
