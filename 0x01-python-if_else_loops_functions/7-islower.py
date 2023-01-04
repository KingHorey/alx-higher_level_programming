#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if value < 91 and value >= 65:
        return True
    else:
        return False
