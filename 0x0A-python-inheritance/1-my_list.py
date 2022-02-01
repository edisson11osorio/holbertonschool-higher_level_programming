#!/usr/bin/python3
"""
class MyList that inherits from list:
"""


class MyList(list):
    """
    Define MyList that is a subclass
    of the class list
    """
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
