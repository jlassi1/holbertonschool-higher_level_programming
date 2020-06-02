#!/usr/bin/python3
"""module of rectangle"""


class BaseGeometry:
    """function area that raises an Exception with the message"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that check if the value is integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialization method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
