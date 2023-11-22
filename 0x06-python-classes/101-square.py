#!/usr/bin/python3

"""
No modules imported
"""


class Square:
    """Create a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        returns the value of self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets self.__size is conditions are met
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        returns self.__position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        assigns self.__position if the conditions are met
        """
        if isinstance(value, tuple) is False or len(value) != 2 or\
                not all(isinstance(val, int) for val in value) or\
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """
        returns the area of a square
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """representation of print()"""
        if self.__size == 0:
            return ""
        if self.__size != 0:
            square = ""
            for i in range(self.__position[1]):
                square += "\n"
            for i in range(self.__size):
                square += " " * self.__position[0] + "#" * self.__size + "\n"

        return (square.rstrip())
