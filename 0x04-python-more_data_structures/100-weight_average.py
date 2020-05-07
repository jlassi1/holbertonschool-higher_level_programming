#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum = 0
    average = 0
    for i in my_list:
        sum += i[0] * i[1]
        average += i[1]
    return (sum / average)
