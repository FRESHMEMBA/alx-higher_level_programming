#!/usr/bin/python3
"""
Defines 2 functions: one to validate matrices, one to multiply two matrices
"""


def validate_matrix(matrix, arg_name):
    """
    Validates a matrix to ensure it meets the required criteria.

    Parameters:
    - matrix (list): The matrix to be validated.
    - arg_name (str): The name of the argument being validated.

    Raises:
    - TypeError: If the matrix is not a list, or if it contains elements that are not lists, integers, or floats.
    - ValueError: If the matrix is empty.
    - TypeError: If the rows of the matrix are not of the same size.

    Returns:
    - None
    """
    if not isinstance(matrix, list):
        raise TypeError(f"{arg_name} must be a list")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{arg_name} must be a list of lists")
    if matrix == [] or matrix == [[]]:
        raise ValueError(f"{arg_name} can't be empty")
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError(f"{arg_name} should contain only integers or floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError(f"each row of {arg_name} must be of the same size")


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Parameters:
    - m_a (list): The first matrix to be multiplied.
    - m_b (list): The second matrix to be multiplied.

    Raises:
    - TypeError: If either m_a or m_b is not a valid matrix.
    - ValueError: If the number of columns in m_a is not equal to the number of rows in m_b.

    Returns:
    - list: The resulting matrix after multiplying m_a and m_b.
    """
    validate_matrix(m_a, 'm_a')
    validate_matrix(m_b, 'm_b')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

