#!/usr/bin/python3
"""module"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file"""
    with open(filename, encoding="UTF8") as myfile:
        lineNum = 0
        while True:
            if not myfile.readline():
                break
            lineNum += 1
    return lineNum
