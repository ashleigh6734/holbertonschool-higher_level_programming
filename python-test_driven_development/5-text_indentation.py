#!/usr/bin/python3
"""
This module defines a function that prints text with indentation.

It inserts two new lines after each '.', '?' or ':' character,
and trims leading/trailing spaces from each printed line.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'.

    Args:
        text: The input string to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    buffer = ""
    for char in text:
        buffer += char
        if char in delimiters:
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip())
