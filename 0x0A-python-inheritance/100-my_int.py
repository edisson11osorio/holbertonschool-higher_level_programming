#!/usr/bin/python3
"""class Myint
"""


class MyInt(int):
    def __eq__(self, other):
        """
        Comparison using == operator __eq__ method
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Comparison using != operator __ne__ method
        Difference
        """
        return int(self) == int(other)
