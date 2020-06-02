#!/usr/bin/python3
""" module of square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initialization method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ the string return from class Rectangle"""
        return "[Saquare] {}/{}".format(self.__size, self.__size)
