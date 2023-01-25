#!/usr/bin/python3

"""
No Modules imported
"""


class Square:
    """Class gets the coordinates of a square and
    makes uses of getters and setters"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            i = 0
            while i < self.__size:
                for j in range(self.position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print()
                i += 1
