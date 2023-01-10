#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inner in matrix:
        for outer in inner:
            print("{:d}".format(outer), end=" ")
        print()
