#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            value = ord(i) - 32
            print('{:c}'.format(value), end="")
        else:
            print('{:c}'.format(ord(i)), end="")
