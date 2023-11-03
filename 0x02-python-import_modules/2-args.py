#!/usr/bin/python3
import sys


def main():

    i = 1
    if len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

    for num in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(num, sys.argv[i]))
        i += 1


if __name__ == "__main__":
    main()
