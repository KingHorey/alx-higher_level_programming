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
        if value is True:
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
