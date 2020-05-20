#!/usr/bin/python3
"""a documentation of my moddules"""


class Square:
    """a documentation of my class """

    def __init__(self, size=0, position=(0, 0)):
        """ check if size is un interege"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        """check if size is a value > then 0"""
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        else:
            self.__position = position

    def area(self):
        """ function tha return the current square area """
        return self.__size ** 2

    """ the getter method """
    @property
    def size(self):
        "function that return the size"""
        return self.__size

    @property
    def position(self):
        return self.__position

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

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        else:
            self.__position = value

    def my_print(self):
        """function that print the square with the character #: """
        if self.__size == 0:
            print()
            return
        for l in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print('#', end="")
            print()

    def __str__(self):
        """function that Return a string\
        containing a printable representation of an object"""
        s = ""
        if self.__size == 0:
            return ""
        for l in range(self.__position[1]):
            s += '\n'
        for i in range(self.__size):
            for j in range(self.__position[0]):
                s += " "
            for k in range(self.__size):
                s += '#'
            s += '\n'
        s = s[:-1]
        return s
