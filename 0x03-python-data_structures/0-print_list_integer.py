#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = len(my_list)
    i = 0
    while x:
        print("{:d}".format(my_list[i]))
        x -= 1
        i += 1
