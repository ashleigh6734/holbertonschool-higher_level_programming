#!/usr/bin/python3
"""
Module: task_01_pickle.py
"""


import pickle


class CustomObject:
    """Defining the CustomObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a formatted style."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(csl, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
