#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    result = []

    if len1 == 1 and len2 == 1:
        for i in range(0, 2):
            if i < 1:
                num = 0
                num += tuple_a[0]
                num += tuple_b[0]
                result.append(num)
            else:
                result.append(0)
    elif len1 == 1:
        for i in range(0, 2):
            if i == 1:
                result.append(tuple_b[i])
            else:
                num = 0
                num += tuple_a[i]
                num += tuple_b[i]
                result.append(num)
    elif len2 == 1:
        for i in range(0, 2):
            if i == 1:
                result.append(tuple_a[i])
            else:
                num = 0
                num += tuple_a[i]
                num += tuple_b[i]
                result.append(num)
    elif len1 == 0 and len2 == 0:
        for i in range(0, 2):
            result.append(0)
    elif len2 == 0:
        for i in range(0, 2):
            result.append(tuple_a[i])
    elif len1 == 0:
        for i in range(0, 2):
            result.append(tuple_b[i])
    else:
        for i in range(0, 2):
            num = 0
            num += tuple_a[i]
            num += tuple_b[i]
            result.append(num)

    results = tuple(result)
    return results
