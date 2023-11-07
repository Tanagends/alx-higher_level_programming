#!/usr/bin/python3
"""Module for writing string to file"""


def write_file(filename="", text=""):
    """"writes to a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
