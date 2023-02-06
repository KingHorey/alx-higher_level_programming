#!/usr/bin/python3

"""NO modules imported"""


def is_same_class(obj, a_class):
    """This function returns True if obj is an instance of a_class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
