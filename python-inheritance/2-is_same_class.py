#!/usr/bin/python3
"""
Write a function that returns True if the object is exactly an instance
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) == a_class
