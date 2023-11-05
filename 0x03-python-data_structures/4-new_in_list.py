#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    rng = len(my_list)
    a = my_list.copy()
    for i in range(0, rng):
        if idx < 0 or idx > (rng - 1):
            return a
        elif i == idx:
            a[idx] = element
            return a
