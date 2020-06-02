#!/usr/bin/python3
""" module my_int"""


class MyInt(int):
    """subclass MyInt"""
    def __init__(self, x):
        """initialization method"""
        self.x = x

    def __eq__(self, other):
        return self.x != other

    def __ne__(self, other):
        return self.x == other
