#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rng = len(matrix)
    for i in matrix:
        sec_rng = len(i)
        for x in range(0, sec_rng):
            if x < (sec_rng - 1):
                print("{:d}".format(i[x]), end=" ")
            else:
                print("{:d}".format(i[x]), end="")
        print()
