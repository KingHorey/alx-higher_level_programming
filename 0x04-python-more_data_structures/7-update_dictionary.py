#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not a_dictionary:
        return 0
    else:
        a_dictionary.update({key: value})

    return (a_dictionary)
