#!/usr/bin/python3
"""a documentation of my moddules"""


class Square:
    """a documentation of my class """
    def __init__(self, size=0):
        """ check if size is un interege"""
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError('size must be an number')
        """check if size is a value > then 0"""
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.size = size

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

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
