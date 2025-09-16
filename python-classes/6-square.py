#!/usr/bin/python3
"""Module that defines a Square class with size, position, area, and print capabilities"""

class Square:
    """Represents a square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance

        Args:
            size (int): size of the square's sides
            position (tuple): tuple of 2 positive integers representing the position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation

        Args:
            value (int): new size value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation

        Args:
            value (tuple): tuple of 2 positive integers

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters, respecting position

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        print("\n" * self.__position[1], end="")

        # Print each row with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
