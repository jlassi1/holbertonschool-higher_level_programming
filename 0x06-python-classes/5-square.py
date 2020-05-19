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

    """ the getter method """
    @property
    def size(self):
        "function that return the size"""
        return self.__size

    """ the setter method"""
    @size.setter
    def size(self, value):
        """function that check the value if it interge and > 0"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """function that print the square with the character #: """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
