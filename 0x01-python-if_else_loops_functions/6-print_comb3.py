#!/usr/bin/python3
f_digit = 0
while f_digit < 9:
    for i in range(1, 10):
        i += f_digit
        if f_digit > 0 and f_digit < 8 and i <= 9:
            print("{:d}{:d}".format(f_digit, i), end=", ")
        elif f_digit == 0:
            print("{:d}{:d}".format(f_digit, i), end=", ")
        elif f_digit == 8 and i == 9:
            print("{:d}{:d}".format(f_digit, i))
    f_digit += 1
