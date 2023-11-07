#!/usr/bin/python3
"""My Serialization Module"""
import json


def to_json_string(my_obj):
    """Serializes object"""
    return str(json.dumps(my_obj))
