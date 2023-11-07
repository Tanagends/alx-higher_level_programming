#!/usr/bin/python3
"""My Serialization Module"""

"""Json Module"""
import json

def to_json_string(my_obj):
    """Serializes object"""
    return json.dumps(my_obj)
