#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return ()
    rng = len(my_list)
    for i in range(0, rng):
        i = (rng - 1) - i
        print("{:d}".format(my_list[i]))
