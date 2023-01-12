#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return 0
    else:
        new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return (dict(new_dict))
