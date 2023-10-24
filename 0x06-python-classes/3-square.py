#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
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

    def area(self):
        """Computes square area"""
        return self.__size ** 2 
