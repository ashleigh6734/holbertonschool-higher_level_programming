#!/usr/bin/python3
"""
This module defines a function for safely adding two numbers.

It validates that both inputs are integers or floats, casts floats to integers,
and raises appropriate exceptions for invalid types. This ensures consistent
behavior and type safety in arithmetic operations.
"""

def add_integer(a, b=98):
    """
    Adds two numbers after validating their types.

    This function accepts two arguments, which must be integers or floats.
    Floats are cast to integers before addition. If either argument is not
    a number, a TypeError is raised.

    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
