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
    i = 0
    s = ""
    while i < len(text):
        if '?' in text[i] or ':' in text[i] or '.' in text[i]:
            s += text[i] + '\n\n'
            i += 2
            if i == len(text) - 1:
                break
        s += text[i]
        i += 1
    print("{}".format(s))
