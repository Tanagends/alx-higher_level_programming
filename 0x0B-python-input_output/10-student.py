#!/usr/bin/python3
"""My Module for Student class"""


class Student:
    """class defining a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of an instance"""
        if isinstance(attrs, list) and not False in\
                [True if isinstance(el, str) else False for el in attrs]:
            new_dict = dict(filter(lambda key, val: key in attrs, attrs)
            return new_dict
            
        return self.__dict__
