#!/usr/bin/python3
"""This function divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div"""
    my_matrix = []
    len_row = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("Division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
        my_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            my_row.append(round(element / div, 2))
        my_matrix.append(my_row)
    return my_matrix
