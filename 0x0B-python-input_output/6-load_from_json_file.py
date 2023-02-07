#!/usr/bin/python3

""" import json module"""
import json


def load_from_json_file(filename):
    """ loads a json file and create python object"""
    with open(filename, 'r') as f:
        python_obj = json.load(f)
        return (python_obj)
