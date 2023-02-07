#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""Import the Rectangle class, for operations"""


class Square(Rectangle):
    """ """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        result = "[" + self.__class__.__name__ + "] "
        result += str(self.__size) + "/" + str(self.__size)
        return result
