#!/usr/bin/python3

"""No modules imported"""


def say_my_name(first_name, last_name=""):
    """ Function receives one or two arguments and prints
    out 'My name is {first_name} {last_name}
    first_name and last_name have to be a string else a TypeError is raised
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
