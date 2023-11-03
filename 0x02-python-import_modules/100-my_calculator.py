#!/usr/bin/python3

import sys
from calculator_1 import add, mul, div, sub


def calculate():
    """ handles basic arithmetic """
    keys = ["*", "/", "+", "-"]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in keys:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        arg_1 = sys.argv[1]
        arg_2 = sys.argv[3]
        operator = sys.argv[2]
        if sys.argv[2] == "*":
            result = mul(int(arg_1), int(arg_2))
            print("{} {} {} = {}".format(arg_1, operator, arg_2, result))
        elif sys.argv[2] == "+":
            result = add(int(arg_1), int(arg_2))
            print("{} {} {} = {}".format(arg_1, operator, arg_2, result))
        elif sys.argv[2] == "/":
            result = div(int(arg_1), int(arg_2))
            print("{} {} {} = {}".format(arg_1, operator, arg_2, result))
        elif sys.argv[2] == "-":
            result = sub(int(arg_1), int(arg_2))
            print("{} {} {} = {}".format(arg_1, operator, arg_2, result))


if __name__ == "__main__":
    calculate()
