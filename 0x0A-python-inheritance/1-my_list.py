#!/usr/bin/python3
""" module of print_sorted"""


class MyList(list):
    """a class that inherits from list:"""
    def print_sorted(self):
        """function that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
