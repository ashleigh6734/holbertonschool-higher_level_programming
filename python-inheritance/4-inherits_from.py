#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class, else False."""
    return issubclass(obj, a_class)
