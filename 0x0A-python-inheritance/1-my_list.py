#!/usr/bin/python3
""" module of print_sorted"""


class MyList(list):
    """a class that inherits from list:"""
    def print_sorted(self):
        print(sorted(self))
