#!/usr/bin/python3

"""No modules imported"""


class Square:
    """Class calculates the area of a square"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
