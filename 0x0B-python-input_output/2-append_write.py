#!/usr/bin/python3

""" No modules imported """


def append_write(filename="", text=""):
    """ Function appends text to an existing file """
    with open(filename, 'a', encoding="UTF-8") as f:
        return (f.write(text))
