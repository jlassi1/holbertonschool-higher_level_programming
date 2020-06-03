#!/usr/bin/python3
"""module"""
import os


def read_lines(filename="", nb_lines=0):
    """function that returns the number of lines of a text file"""
    with open(filename, encoding="UTF8") as myfile:
        if nb_lines <= 0:
            while myfile.readline():
                print(myfile.readline())
        i = 0
        while i < nb_lines:
            print(myfile.readline())
            i += 1
