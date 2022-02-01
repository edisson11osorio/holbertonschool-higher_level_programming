#!/usr/bin/python3
"""
function that returns True if the object is exactly an
instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Return if an object is an
    instance of the class
    """
    return type(obj) is a_class
