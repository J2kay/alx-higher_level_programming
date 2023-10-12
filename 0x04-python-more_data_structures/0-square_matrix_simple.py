#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    matrix_copy = [row.copy() for row in matrix]
    result = list(
            map(
                lambda row: list(
                    map(lambda x: x ** 2, row)
                ),
                matrix_copy
            )
    )
    return result
