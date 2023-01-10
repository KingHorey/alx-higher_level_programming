#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    lgth = len(my_list)
    val = 0
    for i in range(0, lgth):
        if my_list[i] >= val:
            val = my_list[i]
    return (val)
