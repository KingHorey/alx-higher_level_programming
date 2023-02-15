#!/usr/bin/python3

""" import json to handle creation of json strings and os for file validation
"""
import json
import os.path


class Base:
    """ Base class to be used as a package for other
    files
    class has a private class attribute to count the number
    of instances created when is None
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instance initialiser, setting the value of
        self.id

        Conditions:
        if id is None, the private class attribute is incremented,
        and self.id takes on the value of the class attribute
        ex:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

        Otherwise, self.id takes on the value of id that was passed
        during instantiation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def nb_objects(self):
        """ returns number of objects that has been created when instances of
        the subclass Base are made
        """
        return (Base.__nb_objects)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON string
        Args: list_dictionaries:
        a list of dictionaries of instance attribues

        Conditions:
        if list_dictionaries is none, an empty list presented as
        a string is returned
        """
        if list_dictionaries is None:
            return "[]"
        json_rep = json.dumps(list_dictionaries)
        return (json_rep)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string from a file (class_name).json
        Args: list_objs is a list of instancesthat inherits
        from Base

        Conditions:
        if list_objs is empty, an empty list is written into the file.
        Otherwise, the content is overwritten with the new instance
        """
        filename = str(cls.__name__) + ".json"
        if list_objs is None or len(list_objs) <= 0:
            result = []
            with open(filename, mode='w', encoding="UTF-8") as f:
                f.write(str(result))
        else:
            with open(filename, mode='w', encoding="UTF-8") as f:
                result = []
                for i in list_objs:
                    d = i.to_dictionary()
                    result.append(d)
                    data = cls.to_json_string(result)
                f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """ Returns a python list object from a json string
        Args:
        json_string is a json string representation that is to be
        converted to a serializable python object.

        Conditions:
        if json_string is None, an empty list is returned
        """
        if json_string is None:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ creates an instance, diff from the normal instance
        Args:
        **dictionary: kwargs containing key-value pairs to be
        used in instantiation
        """
        if cls.__name__ is not "Square":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances, by creating a new instance
        function reads a file (class_name).json if it exists and writes
         into it. Otherwise, it returns an empty list object
        """
        filename = str(cls.__name__) + ".json"
        result = []
        if not os.path.isfile(filename):
            return (result)
        with open(filename, encoding="utf-8") as f:
            jstring = f.read()
            temp_save = cls.from_json_string(jstring)
        result = [cls.create(**i) for i in temp_save]
        return (result)
