#!/usr/bin/python3
def no_c(my_string):
    empty = ""
    for string in my_string:
        if string == "c" or string == "C":
            continue
        else:
            empty += string

    return empty
