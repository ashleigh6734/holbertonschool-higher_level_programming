#!/usr/bin/python3
"""Module for appending in a file"""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
