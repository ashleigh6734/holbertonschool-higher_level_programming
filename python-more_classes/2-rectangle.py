#!/usr/bin/python3
"""
Module for class "Rectangle"
"""


class Rectangle:
    """
    class that defines a Rectangle by: (based on 0-Rectangle.py)
    Args:
      width (int): width of a side of the Rectangle

    Returns:
      nothing
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with a given width
        Args:
          width (int): width of a side of the Rectangle

        Returns:
          nothing
        """
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    """getters"""
    @property
    def width(self):
        """ Retrieves the width of the Rectangle
        """
        return self.__width

    @property
    def height(self):
        """ Retrieves the width of the Rectangle
        """
        return self.__height

    """setters"""
    @width.setter
    def width(self, value):
        """ Sets the width of the Rectangle
        Args:
          value (int): width of a side of the Rectangle

        Returns:
          nothing
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the width of the Rectangle
        Args:
          value (int): width of a side of the Rectangle

        Returns:
          nothing
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
