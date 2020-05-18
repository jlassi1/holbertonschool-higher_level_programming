#!/usr/bin/python3
def roman_to_int(r):
    if type(r) is not str or r is None:
        return 0
    res = 0
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(r)):
        if i < len(r) - 1 and r_dict[r[i]] < r_dict[r[i + 1]]:
            res -= r_dict[r[i]]
        else:
            res += r_dict[r[i]]
    return res


"""
    if type(roman_string) != str or not roman_string:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    init = 0
    before = 0
    total = 0
    for i in range(len(roman_string)):
        init = dict[roman_string[i]]
        if init > before:
            total = total + init - 2 * before
        else:
            total = total + init
        before = init
    return total
"""
