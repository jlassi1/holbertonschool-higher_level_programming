#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base
import json


class Rectangle(Base):
    """ subclass Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("heigth must be an integer")
        if value <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(y,int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function that calculate the area of Rectangel"""
        return self.height * self.width

    def display(self):
        """function that display the area of Rectangle with #"""
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, "#" * self.width)

    def __str__(self):
        """ the string return from class Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id,
                    self.x,
                    self.y,
                    self.width,
                    self.height
                )

    def update(self, *args, **kwargs):
        """"Update the class Rectangle"""
        attr = ["id", "width", "height", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        if kwargs is not None or args is None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """function that eturns the dictionary representation of a Rectangle"""
        """return self.__dict__"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }
