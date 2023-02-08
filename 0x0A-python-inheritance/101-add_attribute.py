#!/usr/bin/python3

"""No modules"""


def add_attribute(objects, key, value):
    """ Function sets an attribute to a class if possible
    and raises a TypeError if not possible"""

    if not hasattr(objects, "__dict__"):
        raise TypeError("can't add new attribute")
    attr = setattr(objects, key, value)
    return (attr)
