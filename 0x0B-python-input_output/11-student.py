#!/usr/bin/python3
""" NO modules imported """


class Student:
    """
    Defines a student class and can initialise the
    details of the student into an object that can
    be saved as a JSON file
    """

    def __init__(self, first_name, last_name, age):
        """initialise instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns a dictionary representation of
        the instance"""
        if attrs and isinstance(attrs, list):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return (self.__dict__)

    def reload_from_json(self, json):
        """replace attributes of instance"""
        self.__dict__ = json
        return self.__dict__
