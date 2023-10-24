#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates the square class

        Args:
            __size: the size of the square defined.
        Raises:
            TypeError: if size is not integer.
            ValueError: If size < 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """Retrives a square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """"retrieves plane position of a square
        Raises:
            TypeError: if value not a tuple if 2 ints
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of a square
        Args: value as a tuple of two integers
        Raises:
            TypeError: if not a tuple of two positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or False in [
                True if num >= 0 and type(num) == int else False for num in value]:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Computes square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints square as #'s or newline if size is 0"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
