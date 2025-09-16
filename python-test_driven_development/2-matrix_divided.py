#!/usr/bin/python3
"""
This module divides all elements of a matrix

Matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats This ensures consistent
behavior and type safety in arithmetic operations.
"""

def matrix_divided(matrix, div):
    """
    Divides a matrix.

    All elements of the matrix should be divided by div, rounded to 2 decimal places.

    Returns:
    A new matrix.

    Raises:
    TypeError: if rows of the matrix are not the same size or not an integer or float.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
