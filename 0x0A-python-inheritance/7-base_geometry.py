#!/usr/bin/python3

"""NO modules imported"""


class BaseGeometry:
    """
    Geometry class for further operations
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the information that is provided"""
        if not isinstance(name, str):
            raise TypeError("Name is not a string")
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
