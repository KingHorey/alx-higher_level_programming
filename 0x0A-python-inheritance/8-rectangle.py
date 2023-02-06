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
