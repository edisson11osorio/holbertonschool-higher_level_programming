#!/usr/bin/python3
"""Square class"""


class Square:
    """Define Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square attribute"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get position values"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set tuple value"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Define Square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the Square with #"""
        if self.__size == 0:
            print("")
            return
        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
