#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written"""

    with open(filename, mode="w", encoding="UTF8") as myfile:
        myfile.write(text)
        num_char = 0
        for word in text:
            for char in word:
                num_char += 1
    return num_char
