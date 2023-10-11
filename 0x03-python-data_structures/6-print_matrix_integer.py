#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        for items in range(len(row)):
            if items != len(row) - 1:
                print("{:d}".format(row[items]), end=" ")
            else:
                print("{:d}".format(row[items]))
