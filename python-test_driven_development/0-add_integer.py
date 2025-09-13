#!/usr/bin/python3
"""
This module provides a function to add two integers.

It validates input types and casts floats to integers before performing the addition.

    Adds two integers after validating and casting inputs.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The integer result of a + b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
def add_integer(a, b=98):

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
