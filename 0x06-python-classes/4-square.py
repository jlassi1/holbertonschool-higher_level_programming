#!/usr/bin/python3
"""a documentation of my moddules"""


class Square:
    """a documentation of my class """
    def __init__(self, size=0):
        """ check if size is un interege"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        """check if size is a value > then 0"""
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ function tha return the current square area """
        return self.__size ** 2

    @property
    def size(self):
        """ the getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ the setter method"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
