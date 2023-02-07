#!/usr/bin/python3

"""import Json module"""
import json


def save_to_json_file(my_obj, filename):
    """ write an onject into a text file using JSON representation"""
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)
