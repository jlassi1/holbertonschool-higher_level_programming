#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ subclass Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization method"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the string return from class Square"""
        return "[Square] ({}) {}/{} - {}".format(
                    self.id,
                    self.x,
                    self.y,
                    self.size
                )

    @property
    def size(self):
        """getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        super().width = value
        super().height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """"Update the class Square"""
        attr = ["id", "size", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        if kwargs is not None or args is None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """function that eturns the dictionary representation of a Square"""
        """return self.__dict__"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.size
            }
