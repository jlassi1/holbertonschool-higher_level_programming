#!/usr/bin/python3
""" module of square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initialization method"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """function that return area of square"""
        return self.__size ** 2

    def __str__(self):
        """ the string return from class Rectangle"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
