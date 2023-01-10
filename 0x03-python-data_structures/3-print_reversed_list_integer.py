#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rng = len(my_list)
    if my_list is None:
        return
    for i in range(0, rng):
        i = rng - i
        print("{:d}".format(i))
