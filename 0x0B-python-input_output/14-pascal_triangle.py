#!/usr/bin/python3
"""module"""


def pascal_triangle(n):
    """ Pascal's Triangle """
    if n <= 0:
        return []

    T = [[1] * p for p in range(1, 1 + n)]
    for i in range(n):
        for k in range(i):
            if k == 0 or k == i:
                T[i][k] = 1
            else:
                T[i][k] = T[i - 1][k - 1] + T[i - 1][k]
    return T
