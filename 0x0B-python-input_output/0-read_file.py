#!/usr/bin/python3

""" Imports sys module """


def read_file(filename=""):
    """ This function reads information in a txt file and prints to stdout"""

    with open(filename, encoding="UTF8") as f:
        print(f.read(), end='')
