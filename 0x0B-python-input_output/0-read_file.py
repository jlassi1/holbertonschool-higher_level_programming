#!/usr/bin/python3
"""module"""
import os


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="UTF8") as myfile:
        print(myfile.read(), end="")
