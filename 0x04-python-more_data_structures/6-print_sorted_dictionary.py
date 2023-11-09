#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return 0
    else:
        for x, y in sorted(a_dictionary.items()):
            print("{:s}:".format(x), y)
