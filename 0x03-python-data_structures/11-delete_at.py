#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lgth = len(my_list)
    if idx < 0 or idx > lgth or my_list is None:
        return (my_list)
    else:
        new_list = my_list
        i = 0
        for i in range(0, lgth):
            if i != idx:
                new_list[i] = my_list[i]
            else:
                del my_list[i]

    return (new_list)
