#!/usr/bin/python3
"""
Program that add two numbers a and b
a and b must be integer
return the sum of a + b
"""


def add_integer(a, b=98):
    """ function that add two number a and b
    check if a and b are number
    return sum int(a) + int(b)"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
