#!/usr/bin/python3
"""Class Square thet defines a square"""


class Square:
    """Instantiation a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
