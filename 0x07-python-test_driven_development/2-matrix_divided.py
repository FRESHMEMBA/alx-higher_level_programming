#!/usr/bin/python3
"""
"""

def matrix_divided(matrix, div):
    """
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
