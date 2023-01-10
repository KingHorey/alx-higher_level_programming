#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    result = []

    if len2 == 1:
        for i in range(0,2):
            if i == 1:
                result.append(tuple_a[i])
            else:
                num = 0
                num += tuple_a[i]
                num += tuple_b[i]
                result.append(num)
    elif len2 == 0:
        for i in range(0, 2):
            result.append(tuple_a[i])
    else:
        for i in range(0, 2):
            num = 0
            num += tuple_a[i]
            num += tuple_b[i]
            result.append(num)

    results = tuple(result)
    return results
