#!/usr/bin/python3
"""Function that returns the dictionary description for JSON"""



def class_to_json(obj):
    """Returns the dictionary description for JSON serialization"""
    return obj.__dict__
