#!/usr/bin/python3

""" class Base to be imported """
from models.rectangle import *


class Square(Rectangle):
    """ Square class inherits from Rectanglei """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the value of size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """ sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("width should be an integer")
        if (value <= 0):
            raise ValueError("width should be > 0")
        self.width = value

    def __str__(self):
        """Returns string representation"""
        result = "[" + self.__class__.__name__ + "] "
        result += "(" + str(self.id) + ") "
        result += str(self.x) + "/" + str(self.y) + " - " + str(self.size)

        return (result.strip())

    def update(self, *args, **kwargs):
        """ setting variable number of args """
        arg = ["id", "size", "x", "y"]
        if (args):
            for i in range(len(args)):
                setattr(self, arg[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Function returns the dictionary representation of the object
        """
        output = {attr: getattr(self, attr) for attr in
                  ['id', 'size', 'x', 'y']}
        return (output)
