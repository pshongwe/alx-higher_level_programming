#!/usr/bin/python3
"""
matrix divide class
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    """
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(m)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            result = round(element / div, 2)
            divided_row.append(result)
        divided_matrix.append(divided_row)

    return divided_matrix
