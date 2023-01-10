#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    lgth = len(my_list)
    val = -1
    if len(my_list) == 0:
        return None

    for i in range(0, lgth):
        if my_list[i] >= val:
            val = my_list[i]
    return (val)
