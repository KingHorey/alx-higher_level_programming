#!/usr/bin/python3

"""No modules imported"""


def print_square(size):
    """Function prints a square with the character #

    Arguments:
        size - An integer >= 0 that prints the number of sides
        the square has.

    Error:
        TypeError -
            1. if size is not an integer
            2. if size is a float and less than 0
        ValueError -
            1. if size is less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
