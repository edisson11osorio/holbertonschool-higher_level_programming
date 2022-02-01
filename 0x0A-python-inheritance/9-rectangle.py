#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Instantiation of class Rectangle that
    inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Get the area of Rectangle class
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Return a description of Rectangle
        Returns:[Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
