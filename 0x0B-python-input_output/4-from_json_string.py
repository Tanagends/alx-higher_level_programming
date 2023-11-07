#!/usr/bin/python3
"""My Deserialization Module"""
import json


def to_json_string(my_obj):
    """deserializes object"""
    return json.loads(my_obj)
