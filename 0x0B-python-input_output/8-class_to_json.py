#!/usr/bin/python3
"""Returns the dictionary representation with simple data structure
for JSON serialization of an object
"""
def class_to_json(obj):
    """returns dict representaion of object"""
    return obj.__dict__
