#!/usr/bin/python3
import sys


def main():

    i = 1
    result = 0

    for num in range(1, len(sys.argv)):
        result += int(sys.argv[i])
        i += 1
    print("{:d}".format(result))


if __name__ == "__main__":
    main()
