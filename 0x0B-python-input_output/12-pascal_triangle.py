#!/usr/bin/python3

""" NO modules imported"""


def pascal_triangle(n):
    """Creates a pascal triangle in a list"""

    result = []
    if n <= 0:
        return result

    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)

    return result
