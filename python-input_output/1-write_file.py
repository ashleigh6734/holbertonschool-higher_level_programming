#!/usr/bin/python3
"""Module for writing in a file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
