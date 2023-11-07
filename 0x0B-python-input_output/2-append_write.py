#!/usr/bin/python3
"""Module for appending str to a file"""


def append_write(filename="", text=""):
    """Appends str to file"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
