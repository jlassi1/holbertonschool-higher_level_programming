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
    text = text.strip()
    while i < len(text):
        if '?' in text[i] or ':' in text[i] or '.' in text[i]:
            if i == len(text) - 1:
                s += text[i] + '\n'
                break
            s += text[i] + '\n\n'
            i += 2
           
        s += text[i]
        i += 1
    print("{}".format(s))
