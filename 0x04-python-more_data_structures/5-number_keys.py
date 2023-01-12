#!/usr/bin/python3
def number_keys(a_dictionary):
    if not a_dictionary:
        return 0
    else:
        count = 0
        for i in a_dictionary.keys():
            count += 1

    return count
