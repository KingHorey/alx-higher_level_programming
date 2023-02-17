#!/usr/bin/python3

""" import base class in the models directory """
from models.base import *


class Rectangle(Base):
    """ Rectangle class inherits from Base and carries
    out operations """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Returns the value of x"""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """ prints # self.__width times by self.__height"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" "*self.__x + "#" * self.__width)

    def __str__(self):
        """ override print() function"""
        result = "[" + str(self.__class__.__name__) + "] "
        result += "(" + str(self.id) + ") " + str(self.__x) + "/" +\
            str(self.__y) + " - " + str(self.__width) + "/" +\
            str(self.__height)
        result.strip()
        return (result)

    def update(self, *args, **kwargs):
        """ updates the attributes"""
        details = ["id", "width", "height", "x", "y"]
        j = 0
        if (args):
            for i in args:
                attr_name = details[j]
                setattr(self, attr_name, i)
                j += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary representation of the object"""
        result = {x: getattr(self, x) for x in
                  ['id', 'width', 'height', 'x', 'y']}
        return (result)
