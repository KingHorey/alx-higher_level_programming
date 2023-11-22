#!/usr/bin/python3

"""NO modules imported"""


class Square:
    """Getters and setters are used to set the size
    and find the area of a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """returns .__size"""
        return self.__size

    @size.setter
    def size(self, value):
        """checks if value is valid and sets if True"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Outputs # n times the number of self.__size"""
        if self.__size == 0:
            print()
        i = 0
        while i < self.__size:
            for j in range(self.__size):
                print("#", end="")
            print()
            i += 1
