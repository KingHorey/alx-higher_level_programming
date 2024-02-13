#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if value < 123 and value >= 90:
        return True
    else:
        return False
