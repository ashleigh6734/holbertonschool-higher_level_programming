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

    def to_json(self, attrs=None):
        """ Return dictionary representation
        """
        if attrs is None:
            return self.__dict__
        else:
            a_dict = {}
            for i in attrs:
                try:
                    a_dict[i] = getattr(self, i)
                except AttributeError as e:
                    pass
        return a_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
