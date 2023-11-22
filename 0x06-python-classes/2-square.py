#!/usr/bin/python3

"""NO modules imported"""


class Square:
    """Class defines the size of a square and raises an
    error if an int is not provided"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
