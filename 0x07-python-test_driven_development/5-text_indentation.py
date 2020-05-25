#!/usr/bin/python3
"""
Program that prints a text with 2 new lines after each
of these characters: ., ? and :

"""


def text_indentation(text):
    """
    function check if text is a string then split it in to line
    after each ':' , '.' or '?':
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    for c in text.lstrip():
        string += c
        if c in ":.?":
            print(string, end="\n\n")
            string = ""
    print(string.lstrip(), end='')
