#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    x = x = my_list[0]
    if my_list == "":
        return (None)
    for i in range(len(my_list)):
        if my_list[i] >= x:
            x = my_list[i]
    return (x)
