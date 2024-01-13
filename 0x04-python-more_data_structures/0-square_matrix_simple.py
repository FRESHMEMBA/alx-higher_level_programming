#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for row in matrix:
        row_squared = []
        for n in row:
            row_squared.append(n**2)
        matrix_squared.append(row_squared)
    return matrix_squared