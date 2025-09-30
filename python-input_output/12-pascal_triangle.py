#!/usr/bin/python3

def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        new_row = [1] * (row + 1)
        for j in range(1, row):
            new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        triangle.append(new_row)

    return triangle
