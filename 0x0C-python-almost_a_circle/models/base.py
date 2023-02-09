#!/usr/bin/python3

""" NO modules imported"""


class Base:
    """ Base class to be used as a package for other
    files"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id !=  None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
