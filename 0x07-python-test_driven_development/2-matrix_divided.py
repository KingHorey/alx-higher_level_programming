#!/usr/bin/python3

"""
No modules imported
"""


def matrix_divided(matrix, div):
    """
    The division of a matrix element by div

    Args:
        Matrix - a list of list with the same number of elements
        div - divisor which will be used in dividing matrix elements

    Returns:
        A new matrix with elements divided

    Raises:
        TypeError - if div is not an integer/float
                    if elements of the matrix is Zero or not an int or float
                    if matrix is not of the same size
        ZeroDivisionError -
                    if div is Zero

    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div is None:
        raise TypeError("div cannot be none")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    size = len(matrix[0])
    for i in matrix:
        if len(i) != size:
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        if not all(isinstance(val, (int, float)) for val in i):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    new = map(lambda x: [round(i/div, 2) for i in x], matrix)
    return list(new)
