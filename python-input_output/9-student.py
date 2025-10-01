#!/usr/bin/python3
""" Defining the student class
"""


class Student:
    """ Student Class
    """

    def __init__(self, first_name, last_name, age):
        """ Initiliase class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dictionary representation
        """
        return self.__dict__
