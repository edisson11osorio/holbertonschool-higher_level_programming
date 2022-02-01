#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle
(9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square class
    Instantiation with:
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Implement area method
        Returns:square size
        """
        return self.__size * self.__size
