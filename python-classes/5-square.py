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
        self.__size = size

    def area(self):
        """ Returns the current square area
        """
        return (self.__size * self.__size)

    """getter"""
    @property
    def size(self):
        """ Retrieves the size of the square
        """
        return self.__size

    """setter"""

    @size.setter
    def size(self, value):
        """ Sets the size of the square
        Args:
          value (int): size of a side of the square

        Returns:
          nothing
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        """Prints in stdout the square with the character #:
        if size is 0, prints an empty line
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
