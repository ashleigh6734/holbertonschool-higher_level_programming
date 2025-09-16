#!/usr/bin/python3
"""
Module for class "Square"
"""


class Square:
    """
    class that defines a square by: (based on 0-square.py)
    Args:
      size (int): size of a side of the square

    Returns:
      nothing
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size
        Args:
          size (int): size of a side of the square

        Returns:
          nothing
        """
        if not isinstance(size, int):
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
