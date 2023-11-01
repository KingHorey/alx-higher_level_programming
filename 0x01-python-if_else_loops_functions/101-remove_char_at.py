#!/usr/bin/python3

""" No modules imported """


def remove_char_at(str, n):
    """ Takes a string and modifies it by removing
    a letter in an index"""
    temp_store = []
    for i in str:
        temp_store.append(i)
    if n >= 0 and n < len(temp_store):
        del temp_store[n]
    new_str = "".join(temp_store)
    return (new_str)
