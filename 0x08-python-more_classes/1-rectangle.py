#!/usr/bin/python3

"""No modules imported"""


class Rectangle:
    """ Creates a rectangle based on optional arguments: width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """function returns the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """function sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """function returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
