#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    else:
        new_matrix = matrix.copy()
        result = map(lambda x: [(i**2) for i in x], new_matrix)
        new_matrix = list(result)

    return (new_matrix)
