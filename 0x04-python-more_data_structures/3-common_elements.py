#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1:
        return set_1
    elif not set_2:
        return set_2
    else:
        return (set_1 & set_2)
