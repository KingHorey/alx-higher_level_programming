#!/usr/bin/python3

def safe_print_integer(value):
    try:
        name = int(value)
        print("{:d}".format(name))
        return (True)
    except (ValueError, TypeError):
        return False
