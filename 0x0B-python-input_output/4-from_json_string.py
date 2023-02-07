#!/usr/bin/python3

"""Import JSON module"""
import json


def from_json_string(my_str):
    """ load  a JSON string and return
    a python onject"""

    output = json.loads(my_str)
    return (output)
