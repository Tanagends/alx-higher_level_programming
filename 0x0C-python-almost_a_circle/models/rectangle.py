#!/usr/bin/python3
"""My Rectangle Module"""


"""My base module import"""
Base = __import__("base").Base


class Rectangle(Base):
    """My Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width should be an int")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height should be an int")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        if not isinstance(value, int):
            raise TypeError("x should be an int")
        if value < 0:
            raise ValueError("x must be greater than or equal to 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y"""
        if not isinstance(value, int):
            raise TypeError("y should be an int")
        if value < 0:
            raise ValueError("y must be greater than 0")
        self.__y = value
