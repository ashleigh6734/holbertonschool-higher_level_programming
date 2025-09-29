#!/usr/bin/python3
"""Reads a UTF-8 text file and prints its content to stdout."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        print(f.read())
