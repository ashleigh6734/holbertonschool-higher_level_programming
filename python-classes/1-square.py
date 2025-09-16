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

    def __init__(self, size):
        """
        Initializes the square with a given size
        Args:
          size (int): size of a side of the square

        Returns:
          nothing
        """
        self.__size = size
