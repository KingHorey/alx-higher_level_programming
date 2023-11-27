#!/usr/bin/python3

"""NO modules imported"""


def matrix_mul(m_a, m_b):
    """Matrix multiplication of two martices which must be
    1. Lists
    2. List of lists
    3. List of lists with elements as integers/floats
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a is None:
        raise ValueError("m_a can't be empty")
    if m_b is None:
        raise ValueError("m_b can't be empty")
    for m in m_a:
        if not all(isinstance(x, (int, float)) for x in m):
            raise TypeError("m_a should contain only integers or floats")
    for m in m_b:
        if not all(isinstance(x, (int, float)) for x in m):
            raise TypeError("m_b should only contain integers or floats")
    for i in m_a:
        if not i or len(i) <= 0:
            raise ValueError("m_a can't be empty")
    for i in m_b:
        if not m_b or len(i) <= 0:
            raise ValueError("m_b can't be empty")

    lgth = len(m_a[0])
    for m in m_a:
        if len(m) != lgth:
            raise TypeError("each row of m_a must be of the same size")

    lgth = len(m_b[0])
    for m in m_b:
        if len(m) != lgth:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    i = 0
    invb = []
    while i < len(m_b[0]):
        m = 0
        new_list = []
        while m < len(m_b):
            new_list.append(m_b[m][i])
            m += 1
        invb.append(new_list)
        i += 1

    i = 0
    m = 0
    result = []
    for m in m_a:
        j = 0
        temp_ans = []
        for i in invb:
            k = 0
            ans = 0
            while k < len(i):
                ans += m[k] * i[k]
                k += 1
            temp_ans.append(ans)
        result.append(temp_ans)
        j += 1

    return (result)
