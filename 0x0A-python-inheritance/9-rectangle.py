#!/usr/bin/python3
""" Module of Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialization method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """function that calculate the area of Rectangel"""
        return self.__width * self.__height

    def __str__(self):
        """ the string return from class Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
