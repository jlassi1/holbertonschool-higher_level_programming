#!/usr/bin/python3
"""
Program that print a squarte from '#'


"""


def print_square(size):
    """
    function get size and return square of that size
    size must be an integer and >= 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
