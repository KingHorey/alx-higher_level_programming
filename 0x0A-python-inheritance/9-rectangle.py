#!/usr/bin/python3

""" Import parent class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from the parent class"""
    def __init__(self, width, height):
        """initialise attributes based on integer_validator from
        parent class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Prints the area of a square"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the name of the class with the width ad height"""
        result = "[" + self.__class__.__name__ + "] " + str(self.__width) + "/" + str(self.__height)
        return result
