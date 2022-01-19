#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Write a class that defines a square by: (based on 4-square.py)"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size != 0:
            for token in range(self.size):
                print('#' * self.size)
        else:
            print()
