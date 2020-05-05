#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    while x:
        x -= 1
        print("{:d}".format(my_list[x]))
