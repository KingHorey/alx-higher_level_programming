#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not a_dictionary:
        return None
    if not key:
        return a_dictionary
    if not value:
        return a_dictionary
    else:
        a_dictionary.update({key: value})

    return (a_dictionary)
