#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """ Defines a Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for i in range(self.__height):
            s += str(self.print_symbol) * self.__width + '\n'
        return s[:-1]

    def __repr__(self):
        return "Rectangle(%r, %r)" % (self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
