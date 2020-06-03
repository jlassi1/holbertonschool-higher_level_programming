#!/usr/bin/python3
"""module"""
from sys import argv
save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file


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

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
