#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    values = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    max = 0
    i = 0
    y = 0
    for x in values:
        if x > max:
            max = x
            y = i
        i += 1
    return keys[y]
