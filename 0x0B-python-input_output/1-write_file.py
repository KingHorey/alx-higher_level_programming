#!/usr/bin/python3

""" NO modules imported"""


def write_file(filename="", text=""):
    """ This function overwrites information if filename
    is an existing file otherwise creates a file and writes
    information inside"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return (f.write(text))
