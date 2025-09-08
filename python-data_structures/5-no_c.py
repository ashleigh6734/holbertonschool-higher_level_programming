#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string.

    Args:
        my_string (str): The string to remove characters from.

    Returns:
        A new string with all characters c and C removed.
    """
    return ''.join(char for char in my_string if char not in ('c', 'C'))
