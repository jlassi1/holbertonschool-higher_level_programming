#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:"""

    with open(filename, mode="a", encoding="UTF8") as myfile:
        myfile.write(text)
        num_char = 0
        for word in text:
            for char in word:
                num_char += 1
    return num_char
