#!/usr/bin/python3
"""My Module for Student class"""


class Student:
    """class defining a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of an instance"""
        return self.__dict__
