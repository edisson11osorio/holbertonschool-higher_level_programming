#!/usr/bin/python3
"""
Function that returns the list of available
attributes and methods of an object:
"""


def lookup(obj):
    """Returns all properties and
    methods of the specified object,
    without vaues"""
    return dir(obj)
