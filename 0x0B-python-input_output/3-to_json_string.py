#!/usr/bin/python3

""" Import JSON module """
import json


def to_json_string(my_obj):
    """ Returns a JSON string of a python object """
    output = json.dumps(my_obj, sort_keys=True)
    return (output)
