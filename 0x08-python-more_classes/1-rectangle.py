#!/usr/bin/python3
"""My Rectangle Module"""

class Rectangle:
    """Defines a rectangle and its operations"""
    
    def __init__(self, width=0, height=0):
        """instantiates a rectangle with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle
        Raises:
            TypeError: if width value is not an integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """retrieves height"""
        return self._height

    @height.setter
    def height(self, value):
        """sets an int value of height otherwise raises a TypeError"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
