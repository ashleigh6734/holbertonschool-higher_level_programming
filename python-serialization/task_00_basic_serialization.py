#!/usr/bin/python3
"""
Module: task_00_basic_serialization
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes data to JSON and saves it to a file.

    Args:
        data: The data to serialize (list, dictionary, etc.).
        filename: The name of the file to save the JSON data.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
