#!/usr/bin/python3
"""Saves a json serialized object into a text file"""
import json


def save_to_json_file(my_obj, filename):
    """saves serialized my_obj in filename"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
