#!/usr/bin/python3
"""Module to json deserialize text file content"""
import json


def load_from_json_file(filename):
    """deserialises json text in file"""
    with open(filename) as file:
        return json.loads(file.read())
