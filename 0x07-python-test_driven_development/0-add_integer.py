#!/usr/bin/python3
"""
Program that add two numbers a and b
a and b must be integer
return the sum of a + b
"""


def check_value(x):
    """check if the number is integer or float"""
    if not isinstance(x, int) and not isinstance(x, float):
        return False
    else:
        return True


def add_integer(a, b=98):
    """ function that add two number a and b
    check if a and b are number
    return sum int(a) + int(b)"""
    if not check_value(a):
        raise TypeError("a must be an integer")
    if not check_value(b):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
