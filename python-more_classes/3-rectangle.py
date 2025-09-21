#!/usr/bin/python3
"""
Module: Rectangle class
    based on 2-rectangle.py
"""


class Rectangle:
    """
    Class: defines a Rectangle object

    Attributes
    Private instance attribute: width
    Private instance attribute: height

    Instance methods
    public : area
    public: perimeter
    """
    # __width = 0
    # __height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (((self.width + self.height) * 2)
                if self.width > 0 and self.height > 0 else 0)

    def __str__(self):
        thing_to_print = ""
        if self.width == 0 or self.height == 0:
            return thing_to_print
        row = '#' * self.width
        for index, i in enumerate(range(self.height)):
            thing_to_print += row
            # if not last:
            if index < len(range(self.height)) - 1:
                thing_to_print += '\n'
        return (thing_to_print)

    # Getters
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # Setters
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
