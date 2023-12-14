#!/usr/bin/python3
"""Defining an empty class"""


class Square:
    """empty sqaure class"""
    def __init__(self, size=0):

        @property
        def size(self):
            return self._size

        @size.setter
        def size(self, value):
            """function to set the size"""
            if not isinstance(self, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self._size = size

    def area(self):
        """function to return area of the square"""
        return pow(self.size, 2)
    
item = Square(6)
print(item.area())

