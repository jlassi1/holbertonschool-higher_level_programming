#!/usr/bin/python3
"""
Matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """ function that return multiplication of two matrix"""
    i = 0
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not isinstance(m_a[i], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b[i], list):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if any(not isinstance(y, (int, float)) for y in i):
            raise ValueError("m_a should contain only integers or floats")
    for i in m_b:
        if any(not isinstance(y, (int, float)) for y in i):
            raise ValueError("m_b should contain only integers or floats")
    for i in m_a:
        if len(i) == len(m_a[0]):
            pass
        else:
            raise TypeError("each row of m_a must be of the same size")
    for i in m_a:
        if len(i) == len(m_a[0]):
            pass
        else:
            raise TypeError("each row of m_a must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_r = [[] for l in range(len(m_a))]
    m = 0
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m += m_a[i][k] * m_b[k][j]
            m_r[i].append(m)
            m = 0
    return m_r
