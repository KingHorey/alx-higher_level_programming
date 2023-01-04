#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if value < 91 and value >= 65:
        print('{:c}'.format(value), "is upper")
    else:
        print('{:c}'.format(value), "is lower")
