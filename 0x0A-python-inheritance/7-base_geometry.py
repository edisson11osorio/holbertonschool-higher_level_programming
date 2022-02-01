#!/usr/bin/python3
"""
Empty class BaseGeometry
"""


class BaseGeometry:
    """
    Define BaseGeometry class
    """

    def area(self):
        """
        Method that raise an error
        Raises: Exception: area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Method that validate argument value
            name (str): any string
            value (int): any integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
