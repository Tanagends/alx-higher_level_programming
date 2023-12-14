#!/usr/bin/python3
"""Defining an empty class"""


class Square:
    """empty sqaure class"""
    def __init__(self, size=0):
        if isinstance(self, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
