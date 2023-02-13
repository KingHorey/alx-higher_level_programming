#!/usr/bin/python3

import json
import os.path
""" Import JSON """


class Base:
    """ Base class to be used as a package for other
    files"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON representation of args"""
        if list_dictionaries is None:
            return "[]"
        json_rep = json.dumps(list_dictionaries)
        return (json_rep)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string to file"""
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
        """ Returns a list of json_string"""
        if json_string is None:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ creates an instance, diff from the normal instance"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances, by creating a new instance"""
        filename = str(cls.__name__) + ".json"
        result = []
        if not os.path.isfile(filename):
            return (result)
        with open(filename, encoding="UTF-8") as f:
            jstring = f.read()
            temp_save = cls.from_json_string(jstring)
        for i in temp_save:
            result.append(cls.create(**i))
        return (result)
