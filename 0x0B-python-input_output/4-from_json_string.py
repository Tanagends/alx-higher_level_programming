#!/usr/bin/python3
import json
"""My Deserialization Module"""


def to_json_string(my_obj):
    """deserializes object"""
    return json.loads(my_obj)
