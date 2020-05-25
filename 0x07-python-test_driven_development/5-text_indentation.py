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
        s += text[i]
        if text[i] in ".?:":
            s += "\n\n"
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
    print(s, end='')
