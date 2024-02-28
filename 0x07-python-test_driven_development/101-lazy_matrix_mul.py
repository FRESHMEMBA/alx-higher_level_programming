#!/usr/bin/python3
"""
Defines a function that multiplies two matrices using numpy
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy.

    Parameters:
        m_a (array-like): The first matrix to be multiplied.
        m_b (array-like): The second matrix to be multiplied.

    Returns:
        array-like: The result of multiplying the two matrices.

    Notes:
        This function uses the numpy library to perform matrix multiplication
        The input matrices are converted to numpy arrays before multiplication
    """
    return np.array(m_a) @ np.array(m_b)