#!/usr/bin/python3
"""module"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, encoding="UTF8") as f:
        s = ""
        for line in f:
            s += line
            if search_string in line:
                s += new_string
    with open(filename, "w", encoding="UTF8") as f:
        f.write(s)
