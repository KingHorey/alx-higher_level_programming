#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)
    rem = num % 10
    print("{:d}".format(rem), end="")
    return (rem)
