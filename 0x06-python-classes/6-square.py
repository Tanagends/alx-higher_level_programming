#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates the square class

        Args:
            __size: the size of the square defined.
            __position: x, y plane square's coordinates.
        Raises:
            TypeError: if size is not integer.
            ValueError: If size < 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if len(position) != 2 or False in [True if type(num) == int else
           False for num in position]:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Retrives a square size"""
        return self.__size

    @property
    def position(self):
        """retrieves the x,y plane position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if len(position) != 2 or False in [True if type(num) == int else
           False for num in position]:
            raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints square as #'s or newline if size is 0"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
