#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    elif len(my_list) == 0:
        return None
    else:
        lgth = len(my_list)
        new_list = []
        for i in range(0, lgth):
            if my_list[i] % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
    return (new_list)
