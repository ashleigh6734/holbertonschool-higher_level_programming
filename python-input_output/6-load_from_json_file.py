#!/usr/bin/python3
"""Module for JSON to obj"""


import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.load(f)
