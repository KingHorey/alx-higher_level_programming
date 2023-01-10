#!/usr/bin/python3
def element_at(my_list, idx):
    num = len(my_list) - 1
    for i in my_list:
        if (idx > num or idx < 0):
            return (None)
        elif i == idx:
            return (my_list[i])
