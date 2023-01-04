#!/usr/bin/python3
def uppercase(str):
    name = ""
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            value = ord(i) - 32
            name += chr(value)
        else:
            name += i
    print("{:s}".format(name))
