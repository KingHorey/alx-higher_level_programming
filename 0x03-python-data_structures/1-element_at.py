#!/usr/bin/python3
def element_at(my_list, idx):
    num = len(my_list)
    for i in range(0, num):
        if (idx > num or idx < 0):
            return (None)
        elif i == idx:
            return (my_list[i])
