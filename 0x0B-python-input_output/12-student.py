#!/usr/bin/python3
"""module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and all(type(i) == str for i in attrs):
            my_dict = {}
            for j in attrs:
                if hasattr(self, j):
                    my_dict[j] = getattr(self, j)
            return my_dict
        return self.__dict__
