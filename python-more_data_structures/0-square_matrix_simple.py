#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.

    Args:
        matrix (list of lists): A list of lists of integers.

    Returns:
        list of lists: A new matrix with the squared values.
    """
    return [[num ** 2 for num in row] for row in matrix]
