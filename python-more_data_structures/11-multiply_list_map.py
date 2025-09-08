#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Multiply all integers of a list by a number.

    Args:
        my_list (list): List of integers.
        number (int): The number to multiply by.

    Returns:
        A new list representing the result of the multiplication.
    """
    return list(map(lambda x: x * number, my_list))
