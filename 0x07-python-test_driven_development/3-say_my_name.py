#!/usr/bin/python3
"""
Program say my name retune "My name is {fist_name} {last_name}"


"""


def say_my_name(first_name, last_name=""):
    """
    function say my name
    first_name and last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
