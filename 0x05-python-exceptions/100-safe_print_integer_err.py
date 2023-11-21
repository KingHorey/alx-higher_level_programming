#!/usr/bin/python3

import sys

""" import sys function to have access to
printing to stderr
"""


def safe_print_integer_err(value):
    """ prints to stdout if value is an integer, otherwise
    prints to stderr
    """
    try:
        print("{:d}".format(value))
        return True
    except TypeError as e:
        sys.stderr.write(f"Exception: {e}\n")
    except ValueError as e:
        sys.stderr.write(f"Exception: {e}\n")
        return False
