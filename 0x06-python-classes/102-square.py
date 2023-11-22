#!/usr/bin/python3

"""
No Module imported
"""


class Square:
    """Class compares two squares"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)) is False:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of a square"""
        return (self.__size ** 2)

    def __lt__(self, y):
        return self.area() < y.area()

    def __gt__(self, y):
        return self.area() > y.area()

    def __eq__(self, y):
        return self.area() == y.area()

    def __ne__(self, y):
        return self.area() != y.area()

    def __ge__(self, y):
        return self.area() >= y.area()

    def __le__(self, y):
        return self.area() <= y.area()
