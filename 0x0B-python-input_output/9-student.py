#!/usr/bin/python3

""" NO modules imported """


class Student:
    """
    Defines a student class and can initialise the
    details of the student into an object that can
    be saved as a JSON file
    """

    def __init__(self, first_name, last_name, age):
        """initialisa instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dictionary representation of
        the instance"""
        return (self.__dict__)
