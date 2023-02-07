#!/usr/bin/python3

""" No modules imported """


def read_file(filename=""):
    """ This function reads information in a txt file and prints to stdout"""

    with open(filename,'r', encoding="UTF-8") as f:
        print(f.read())
