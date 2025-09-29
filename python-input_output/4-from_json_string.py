#!/usr/bin/python3
"""Function that returns the object (string) representation from JSON"""


import json


def from_json_string(my_str):
    """Function that returns the object (string) representation from JSON"""
    return json.loads(my_str)
