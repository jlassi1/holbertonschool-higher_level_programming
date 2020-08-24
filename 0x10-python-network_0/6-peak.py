#!/usr/bin/python3
""" Function find_peak """


def find_peak(list_of_integers):
    """ Function find_peak """
    if list_of_integers is None or list_of_integers == []:
        return None
    for i in range(0, len(list_of_integers)):
        peak = list_of_integers[0]
        if i == len(list_of_integers) - 1:
            break
        """if list_of_integers[i] < list_of_integers[i + 1]\
                and list_of_integers[i] < list_of_integers[i - 1]:
            peak = list_of_integers[i]
            break"""
        if list_of_integers[i] > list_of_integers[i + 1]\
                and list_of_integers[i] > list_of_integers[i - 1]:
            peak = list_of_integers[i]
            break

    return peak
